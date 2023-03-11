
# Adds nickname, gender, and usage data

import json
with open('name_data.json', 'r') as f:
	data = json.load(f)
	nn = data['firstNames']
	ppl = data['personList']

	for i in range(len(nn)):
		ppl[i]['finalName'] = nn[i]
		if ppl[i]['finalName'] == ppl[i]['firstName']:
			ppl[i]['nickName'] = 0
		else:
			ppl[i]['nickName'] = 1

		with open('btn_scraped_data.json', 'r') as b:
			btn = json.load(b)
			try:
				btnnd = btn[ppl[i]['finalName']]
			except:
				pass

			if btnnd:
				ppl[i]['nameGender'] = btnnd['gender']
				ppl[i]['nameUsage'] = btnnd['usage']

	dt = {}
	dt['firstNames'] = nn
	dt['personList'] = ppl

	with open("name_data_billionaires.json", "w") as outfile:
		json.dump(dt, outfile)