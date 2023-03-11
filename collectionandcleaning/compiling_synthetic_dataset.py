
# Adeline Hipps
# March 10, 2023

# This file takes the social security name data from individual json files and compiles a dictionary of lists of names of babies born each year
# that one of the forbes 400 was born


import json
import os


# Getting all birth years
with open('name_data.json', 'r') as f:
	data = json.load(f)
	nn = data['firstNames']
	ppl = data['personList']

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

# Compiling dataset of all names from birthyears
ynls = {} # yearly name lists for men
for year in years:
	ynls[year] = []

ynlsf = {}
for year in years:
	ynlsf[year] = []

path = 'babynames/flat_files/individuals/'
for filename in os.listdir(path): # for every SSA name file
	print(str(filename))
	fp = path + str(filename)
	if '.json' in fp and 'undefined' not in fp and '-m' in fp: # male names
		with open(fp, encoding='utf-8', mode='r') as f:
			nd = json.load(f)

			for year in years:
				if year in nd['values'].keys(): # if that name occurred in that year
					freq = nd['values'][year] # frequency of name in that year
					l = [nd['name']] * freq # list of that name as many times as it occurred in the year

					yl = ynls[year] # list of all names so far that year
					yl.extend(l) # add current name the number of times it occurred

					ynls[year] = yl # update dictionary

	elif '.json' in fp and 'undefined' not in fp and '-f' in fp:  # female names
		with open(fp, encoding='utf-8', mode='r') as f:
			nd = json.load(f)

			for year in years:
				if year in nd['values'].keys(): # if that name occurred in that year
					freq = nd['values'][year] # frequency of name in that year
					l = [nd['name']] * freq # list of that name as many times as it occurred in the year

					yl = ynlsf[year] # list of all names so far that year
					yl.extend(l) # add current name the number of times it occurred

					ynlsf[year] = yl # update dictionary

fin = {}
fin['male'] = ynls
fin['female'] = ynlsf

with open("babies_by_year.json", "w") as outfile:
		json.dump(fin, outfile)










