
setwd("/Users/adelinehipps/Downloads/dsproject")
# Setup
library(car)
library(ggplot2)
library(MASS)
library(leaps)
library(pROC)
library(blorr)
library(caret)
library(modelsummary)
library(dplyr)

use <- read.csv("combined_dataset_usage.csv")
head(use)


### LOGISTIC REGRESSION ###
#remove irrelevant columns for ease of model building
use1 <- subset(use, select = -c(rich, pctyb))
use1$richnum <- as.factor(use1$richnum)

#checking for missingness
sort(colSums(is.na(use1)), decreasing = TRUE)

summary(use1)

# contingency tables making sure there are no 0s
xtabs(~richnum + french, data = use1)
xtabs(~richnum + english, data = use1)
xtabs(~richnum + biblical, data = use1)
xtabs(~richnum + unisex, data = use1)

write.csv(use1, file = "use1.csv")
attach(use1)
use2 <- data.frame(cbind(richnum,french,english,biblical,unisex,pctrank))
use2$richnum <- as.factor(use2$richnum)
detach(use1)

attach(use2)

## First-Order Logistic Regression Model
glm.model<-glm(richnum~french+english+biblical+unisex+pctrank, data = use2, family = "binomial")
summary(glm.model)

## CIs using standard errors
confint.default(glm.model)

# double-checking for multicollinearity
vif(glm.model) #no values above 1.7

## Stepwise Selection Procedure
aic.mod <- stepAIC(glm.model, direction = "both", trace = 0, k = 2)
summary(aic.mod)

# BIC selection
bic.mod <- stepAIC(glm.model, direction = "both", trace = 0, k = log(50))
summary(bic.mod)

## All-subset Selection
x.mod <- cbind(french,english,biblical,unisex,pctrank)
y.mod <- richnum
leap.out <- leaps(x.mod, y.mod, method = c("r2"), nbest = 1)
leap.out$which[leap.out$size==3] # biblical and pctrank

leap.out <- leaps(x.mod, y.mod, method = c("Cp"), nbest = 1)
leap.out$which[leap.out$size==3] # biblical and pctrank

## Interaction Model
int.model<-glm(richnum~.*., data = use2, family = "binomial")
summary(int.model)

# AIC selection (10 terms)
aic.int.mod <- stepAIC(int.model, direction = "both", trace = 0, k = 2)
summary(aic.int.mod)

# BIC selection (same 10 terms)
bic.int.mod <- stepAIC(int.model, direction = "both", trace = 0, k = log(50))
summary(bic.int.mod) # same as aic

#cross validation
set.seed(123)
ctrl <- trainControl(method = "cv",number=10)
cv.fo.aic.model <- train(richnum~french+english+biblical+pctrank, data = use2, method = "glm", trControl = ctrl)
cv.int.model<- train(richnum ~ french+english+biblical+unisex+pctrank+french:english+french:pctrank+
                       english:unisex+english:pctrank+unisex:pctrank, data = use2, method="glm",trControl=ctrl)
print(cv.fo.aic.model)
print(cv.int.model)

## Likelihood ratio test for model comparison
summary(aic.mod)
summary(aic.int.mod)

# Difference in residual deviances
lrt <- 3132.9 - 3072.0
lrt # on 6 degrees of freedom
qchisq(.95, df=6) # the interaction model is better
modelsummary(aic.int.mod, output = "finalmodelsummary.png")

## Likelihood ratio test for goodness-of-fit 
summary(int.model) # 15 parameters
summary(aic.int.mod) # 10 parameters

# Difference in residual deviances
drd <- 3072.0 - 3069.1
drd
qchisq(.95, df=5) # for comparison to deviance for significance
pchisq(drd, 5) # p-value on chi square distribution

## ROC Curve and AUC
pi.hat = predict(aic.int.mod,type="response") #predicted prob
Y.hat = ifelse(pi.hat>0.06,1,0) # dichomotize using 0.06
table(Y.hat,richnum) #confusion matrix

# plotting the ROC curve
plot(roc(richnum,pi.hat))
auc(richnum,pi.hat) # better than random

## Diagnostic plots
par(mfrow=c(2,2))
plot(aic.int.mod)

# Delta Deviance Plot
blr_plot_diag_difdev(
  aic.int.mod,
  point_color = "blue",
  title = "Delta Deviance Plot",
  xaxis_title = "id",
  yaxis_title = "Delta Deviance"
)


### T-test of Popularity ###
t.test(pctrank ~ richnum, var.equal = TRUE) # p-val: 0.2728

### Estimated difference in Proportions ###
rich <- use2[richnum == 2, ]
com <- use2[richnum == 1, ] # common

# French
pp.r.fr <- mean(rich$french) # proportion of rich that are French
pp.c.fr <- mean(com$french)

dpp.fr <- pp.c.fr-pp.r.fr # Difference in proportion for French
dpp.fr

dpp.se.fr <- as.numeric(sqrt(((pp.c.fr*(1-pp.c.fr))/count(rich))-((pp.r.fr*(1-pp.r.fr))/count(com))))
dpp.se.fr # standard error

fr.low <- dpp.fr-2*dpp.se.fr
fr.up <- dpp.fr+2*dpp.se.fr
fr.low # 95% Confidence interval
fr.up

# English
pp.r.en <- mean(rich$english) # proportion of rich that are English
pp.c.en <- mean(com$english)

dpp.en <- pp.c.en-pp.r.en # Difference in proportion for English
dpp.en

dpp.se.en <- as.numeric(sqrt(((pp.c.en*(1-pp.c.en))/count(rich))-((pp.r.en*(1-pp.r.en))/count(com))))
dpp.se.en # standard error

en.low <- dpp.en-2*dpp.se.en
en.up <- dpp.en+2*dpp.se.en
en.low # 95% Confidence interval
en.up

# Biblical
pp.r.bi <- mean(rich$biblical) # proportion of rich that are Biblical
pp.c.bi <- mean(com$biblical)

dpp.bi <- pp.c.bi-pp.r.bi # Difference in proportion for Biblical
dpp.bi

dpp.se.bi <- as.numeric(sqrt(((pp.c.bi*(1-pp.c.bi))/count(rich))-((pp.r.bi*(1-pp.r.bi))/count(com))))
dpp.se.bi # standard error

bi.low <- dpp.bi-2*dpp.se.bi
bi.up <- dpp.bi+2*dpp.se.bi
bi.low # 95% Confidence interval
bi.up
