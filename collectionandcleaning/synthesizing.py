# Adeline Hipps
# March 10, 2023


# after compiling_synthetic_dataset.py

import json
import random

synth = []


# Copied from compiling_synthetic_dataset.py
with open('name_data.json', 'r') as f:
	data = json.load(f)
	nn = data['firstNames']
	ppl = data['personList']
	print(len(ppl))

	years = []
	ywfreq = [] # list of (year, male_frequency, female_frequency)

	for d in ppl:
		by = d['birthYear']
		if by in years:
			for y in ywfreq:
				if y[0] == by:
					ctm = y[1]
					ctf = y[2]
					if d['gender'] == 'M':
						ctm += 1
					elif d['gender'] == 'F':
						ctf +=1
					ywfreq.remove(y)
					ywfreq.append((by, ctm, ctf))

		else:
			years.append(by)
			if d['gender'] == 'M':
				ywfreq.append((by, 1, 0))
			elif d['gender'] == 'F':
				ywfreq.append((by, 0, 1))



with open("babies_by_year.json", 'r') as f2:
	data2 = json.load(f2)
	male = data2['male']
	female = data2['female']

tot = 0

for t in ywfreq:
	year = t[0] # a birthyear
	mfreq = t[1] # number of males on forbes 400 in that year
	tot += mfreq
	ffreq = t[2] # number of females on forbes 400 in that year
	tot += ffreq

	mns = male[year] # male names in that year
	fns = female[year] # female names in that year

	for i in range(mfreq*10):
		i = random.randrange(len(mns))
		synth.append([mns[i], 'm', year])
	for i in range(ffreq*10):
		i = random.randrange(len(fns))
		synth.append([fns[i], 'f', year])

with open("synth_list.json", "w") as outfile:
		json.dump(synth, outfile)

import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from time import sleep
import os

chrome_options = Options()
chrome_options.add_argument("--headless")

def getNameData(query):
	driverpath ='driver/chromedriver'
	service = Service(driverpath)
	driver = webdriver.Chrome(service=service, options=chrome_options)

	url = f"https://www.behindthename.com/name/{query}"
	driver.get(url)

	# wait for the new content to be loaded
	sleep(2)

	# click to get the IPA transcription
	#driver.find_element(By.XPATH, "return toggle_pron").click()

	# Access the content of the page
	htmlPage = driver.page_source
	
	# if a folder with the name of the query doesn't exist, create it, then save the file
	if not os.path.isdir('synthHtmls2'):
		os.mkdir('synthHtmls2')
	with open(f"synthHtmls2/{query}.html", 'w', encoding='utf-8') as output:
		output.write(htmlPage)
		
	# close the instance
	driver.close()

done = []
for n in synth:
	if n[0] not in done:
		getNameData(n[0])
		done.append(n[0])
	else:
		pass










