
from bs4 import BeautifulSoup
import requests
import lxml
import os
import csv
from collections import Counter
import json
import os


def getGender(i):
	"""
	Parses all relevant genders from a 'bs4' object into a list
	"""
	
	gender = []
	if i:
		f = i.find('span', class_='fem')
		m = i.find('span', class_='masc')

		if f:
			gender.append(f.text)
		if m:
			gender.append(m.text)

		return gender

def getIPA(i):
	"""
	Parses all relevant IPA pronunciations from a 'bs4' object into a list
	"""
	try:
		return [f.text for f in i.findAll(class_="prn ipa")]
	except:
		return []

def getUsage(i):
	"""
	Parses all relevant Usages from a 'bs4' object into a list
	"""
	try:
		return [f.text for f in i.findAll(class_="usg")]
	except:
		return []


def scrapePage(name, filename):
	"""
	Takes an input HTML file of a BehindTheName page and
	returns a list of tuples of (name, gender, usage)
	"""
	with open(filename, 'r') as f:
		try:
			soup = BeautifulSoup(f, features="lxml") # creates bs4 object
			gen = getGender(soup)
			#ipa = getIPA(soup)
			use = getUsage(soup)

			return (name, filename, gen, use)
		except: #utf-8 file
			pass

def writeJSON(pagedatalist):
	"""
	Takes the (name, filename, gender, usage) and writes it to a json file
	"""
	dt = {}
	for r in pagedatalist:
		if r:
			rdict = {}
			rdict['name'] = r[0]
			rdict['filename'] = r[1]
			rdict['gender'] = r[2]
			rdict['usage'] = r[3]


			dt[r[0]] = rdict

	with open("btn_scraped_synth_data.json", "w") as outfile:
		json.dump(dt, outfile)



# assign directory
directory = 'synthHtmls2'
nL = []
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	# checking if it is a file
	if os.path.isfile(f):
		name = filename.split('.')[0]
		n = scrapePage(name, f)
		nL.append(n)

writeJSON(nL)








