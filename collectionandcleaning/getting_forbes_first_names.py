# Adeline Hipps
# Feb. 28, 2023

# This file takes in the file 'forbes400.json' and extracts a list of first names

import json
from datetime import datetime

fns = []
dt = []

with open('forbes400.json', 'r') as f:
	data = json.load(f)
	people = data['personList']['personsLists']

	# KEYS FOR EACH PERSON IN people
	# (['name', 'year', 'month', 'uri', 'rank', 'listUri', 'finalWorth',
	# 'category', 'otherCompensation', 'person', 'visible', 'personName',
	# 'age', 'country', 'state', 'city', 'source', 'industries', 'countryOfCitizenship',
	# 'organization', 'timestamp', 'version', 'naturalId', 'position', 'imageExists', 
	# 'selfMade', 'status', 'gender', 'birthDate', 'lastName', 'firstName', 'listDescription',
	# 'title', 'employment', 'date', 'wealthList', 'familyList', 'selfMadeRank', 'residenceStateRegion',
	# 'squareImage', 'bioSuppress', 'csfDisplayFields', 'suppressOnProfiles', 'qas', 'bios', 
	# 'abouts', 'premiumProfile', 'philanthropyScore', 'embargo'])


	for i in people:
		person = {}
		firstName = i['firstName']

		fns.append(firstName)

		person['firstName'] = firstName
		person['lastName'] = i['lastName']
		person['gender'] = i['gender']
		person['birthYear'] = (datetime.utcfromtimestamp(i['birthDate']/1000.0).strftime('%Y-%m-%dT%H:%M:%SZ'))[:4] # converting from unix timestamp to date, then collecting only the year
		person['selfMadeRank'] = i['selfMadeRank']

		dt.append(person.copy())

finD = {}
finD['firstNames'] = fns
finD['personList'] = dt

with open("name_data.json", "w") as outfile:
    json.dump(finD, outfile)




		

