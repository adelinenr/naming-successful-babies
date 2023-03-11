# Takes the combined data sheet in .csv and adds categorical variables for usage languages, as well as categorical for unisex

import csv

with open('combined_dataset_sheet.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	with open('combined_dataset_usage.csv', 'w') as f:
		write = csv.writer(f)
		headings = next(csv_reader)
		headings.append('french')
		headings.append('english')
		headings.append('biblical')
		headings.append('unisex')
		write.writerow(headings)
		for row in csv_reader:
			usage = row[4]
			#print(usage)
			us = [0,0,0]

			if 'French' in usage:
				us[0] = 1
				print(us)

			if 'English' in usage:
				us[1] = 1

			if 'Biblical' in usage:
				us[2] = 1

			row.extend(us)

			if len(row[3])>13:
				row.append(1)
			else:
				row.append(0)

			write.writerow(row)