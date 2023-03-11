# naming-successful-babies

While money is not a barrier for American parents choosing a name for their infant, people colloquially associate certain names with socioeconomic statuses. This difference between common-sounding and wealthy-sounding names is understood to exist, but specific characteristics of the wealthy-sounding names are less clear. Similar prior studies have tried to predict name trends and questioned if a name can predict personality traits or impact a person’s chance of employment.

This research project seeks to identify characteristics commonly associated with the names of the wealthiest Americans in order to demystify what differentiates wealthy names from common names.

Research Questions include: What features are most highly correlated with the first names of the wealthiest Americans? Do the names of the elite follow patterns of prestige from the broader English language? Are wealthy Americans likely to have more common or unusual names than other Americans?

The names of the 400 wealthiest Americans were collected from the Forbes 400 list for 2022. Historical naming data was collected for the years 1880-2021 from the U.S. Social Security Administration (SSA). Global name usages (by current countries and languages, or historical origins) and genders were collected by scraping BehindTheName.com. A dataset of names with the same sex and birth years of the Forbes 400 was created with weighted random selection from the SSA popularity data. Categorical variable of interest were then added based on collected data.

The final dataset has 7700 names, 400 of which are the Forbes 400, each with a birth year, sex of the person, common genders of the name, list of global usages, and the percent of babies born in the United States in the birth year with the same name.


Files:

Datasets:
- individual-names is a small sample of name data collected from the SSA
- forbes400.json includes a small sample of the relevant information on each of the wealthiest Americans
- synth_list.json is all of the people randomly selected from the SSA data to represent common naming conventions
- combined_dataset_usage.csv is the final dataset used for analysis

Collection and Cleaning:
These files need to be reorganized for ease of reuse. Here are the files as they exist in order of use:
- downloading_forbes_data.py scrapes from Forbes.com
- getting_forbes_first_names.py parses the relevant information for this project from all of the gathered Forbes data
- scraping_name_data.py scrapes the Forbes 400 name, gender(s) and usage(s) from BehindtheName
- parsing_name_data_from_html.py takes the Forbes 400 name html pages and compiles them into a dataset
- cleaning_nicknames.py adds a dimension to the Forbes 400 data if the person went by a nickname (i.e. "Bob"), which I manually changed to the full name
- intro_analysis.ipynb shows introductory vizualizations for the Forbes 400 data
- compiling_synthetic_dataset.py takes the social security name data from individual json files and compiles a dictionary of lists of names of babies born each year that one of the forbes 400 was born
- synthesizing.py scrapes the BehindTheName pages for the synthetic dataset
- parsing_and_cleaning_synth.py writes a .json file of some of the relevant data from BTN for the synthetic dataset
- add_synth_frequency.py adds the SSA frequency data to the synthetic dataset
- add_name_frequency.py combines the synthetic and Forbes data into one .csv file
- add_usage_cats.py adds the categorical variables for name usage to the final dataset

Charts:
- biblical, french, and english proportions show the proportion estimated differences
- pctrankpopularitychart.png is a vizualization of the popularity difference between wealthy and common names
- logistic_regression.pdf shows information on the final regression model
- multiplecorrelations.png shows the correlations between each of the variables in the dataset so far
- the Capstone Poster is the poster used for the March 10th draft deadline presentation.

