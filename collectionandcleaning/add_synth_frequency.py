# Takes the synthetic data and adds the percentage of that name for that gender in the US in their birth year according to the SSA, then exports it as a csv

import json
import csv
import os

# Headings for csv outfile
headings = ['name', 'gender', 'birthyear', 'pctyb', 'namegender', 'usage', 'rich']
rows = []


# Adding synthetic people to Dataset
with open("btn_scraped_synth_data.json", "r") as f:
	names = json.load(f)

	with open("synth_list.json", "r") as f2:
		ppl = json.load(f2)

		for person in ppl:
			simplename = person[0].lower()
			gender = person[1]
			birthyear = person[2]

			dpath = 'babynames/flat_files/individuals/' + simplename + '-' + gender + '.json' # SSA filename

			if os.path.isfile(dpath):
				with open(dpath, newline='') as ssa:
					ssad = json.load(ssa)

					try:
						person.append(ssad['percents'][birthyear])
					except:
						person.append(0)

			try: # adding gender

				genders = names[person[0]]['gender']

				for g in genders:
					if 'f' == g:
						genders.remove('f')
						genders.append('Feminine')
					if 'm' == g:
						genders.remove('m')
						genders.append('Masculine')
				person.append(genders) # gender(s) that use the name

			except: # if missing from data collection, fill in sex from SSA
				if 'f' in gender:
					person.append(['Feminine']) 
				if 'm' in gender:
					person.append(['Masculine'])
				else:
					person.append([])
				
			try: # adding usage
				person.append(names[person[0]]['usage']) # place(s) that use the name
			except:
				person.append([]) # empty list

			person.append(0) # not a rich person
			rows.append(person)

# Adding Forbes 400 to Dataset
with open('billionaires_with_ssa.json', 'r') as infile:
	bd = json.load(infile)
	for rich in bd:
		row = []
		row.append(rich['finalName']) # name
		row.append(rich['gender'])
		row.append(rich['birthYear'])

		try:
			row.append(rich['pctYB'])
		except:
			row.append(0)

		try:
			genders = rich['nameGender']
			for g in genders:
				if 'f' == g or 'F' == g:
					genders.remove(g)
					genders.append('Feminine')
				if 'm' == g or 'M' == g:
					genders.remove(g)
					genders.append('Masculine')
			row.append(genders)

		except:
			row.append(rich['gender']) # if missing from data collection, fill in sex from Forbes

		try:
			row.append(rich['nameUsage'])
		except:
			row.append([]) # empty list

		row.append(1) # a rich person
		rows.append(row) # adding to full dataset


# Writing all data to a .csv
with open('combined_dataset.csv', 'w') as f:
	write = csv.writer(f)
	write.writerow(headings)
	write.writerows(rows)





