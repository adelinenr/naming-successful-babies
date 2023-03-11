# Adeline Hipps
# Feb. 28, 2023

# This file uses the wrapper pyforbes to download the 2022 Forbes 400 data into a JSON file

from pyforbes import ForbesList
import json

flist = ForbesList()

billionaires_json = flist.get_json('forbes-400', year=2022)

with open("forbes400.json", "w") as outfile:
    json.dump(billionaires_json, outfile)