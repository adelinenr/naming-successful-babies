# Adeline Hipps
# Feb. 28, 2023

# This file scrapes name data from BehindTheName.com

# Based on code from "Google Search Results for Various Geographical Locations" by Eni Mustafaraj

import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from time import sleep
import os

names = ["Elon", "Jeffrey", "William", "Lawrence", "Warren", "Lawrence", "Sergey", "Steven", "Michael", "James", "Mark", "Robert", "Charles", "Julia", "Alice", "Michael", "Phil", "MacKenzie", "Jacqueline", "John", "Kenneth", "Leonard", "Jeffrey", "Stephen", "James", "Miriam", "Leonard", "Harold", "Abigail", "Lukas", "Thomas", "Raymond", "David", "Eric", "Rupert", "Carl", "Robert", "Steven", "Donald", "Daniel", "Samuel", "Thomas", "John", "Jerral", "David", "George", "Jan", "Jensen", "Stanley", "Laurene", "Diane", "Stephen", "Donald", "Israel", "Shahid", "Philip", "John", "Jeffery", "Robert", "Charles", "Andrew", "Michael", "Autry", "Christy", "Pierre", "Carl", "John", "David", "Marijke", "Pamela", "Valerie", "Victoria", "Eric", "Brian", "Chase", "Patrick", "James", "Blair", "Jay", "Ann", "Leon", "Bernard", "Tamara", "Dustin", "George", "Robert", "Orlando", "Michael", "Ramzi", "Steven", "David", "John", "Nathan", "Rocco", "Tilman", "David", "Nancy", "Harry", "Arthur", "Rick", "Joe", "Leonard", "Tim", "Charles", "Arthur", "James", "Paul", "Gordon", "Henry", "Pauline", "Richard", "Jeff", "Donald", "Leo", "Jack", "Christopher", "Jude", "Don", "Dannine", "Edythe ", "Scott", "Milane", "Philippe", "Igor", "Randa", "John", "David", "Judith", "Paul", "Terrence", "Henry", "George", "Donald", "Daniel", "Trudy", "Edward", "Bruce", "David", "Ralph", "Reinhold", "John", "John", "Marc", "Stephen", "Stanley", "Melinda", "Ted", "Edward", "David", "Kenneth", "Dennis", "Neil", "Thomas", "Ge", "Michael", "David", "Leslie", "Mitchell", "Antony", "Josh", "Ray", "Kenneth", "Douglas", "Karen", "Patrick", "Daniel", "Dirk", "Robert", "Henry", "Ronda", "Micky", "James", "Wesley", "Archie", "Jonathan", "Judy", "Thomas", "Katharine", "Paul", "Margaretta", "Thomas", "Vinod", "George", "Todd", "Richard", "Lynda", "Stewart", "Charles", "Samuel", "Robert", "Daniel", "Jane", "Robert", "Gary", "Mark", "Elizabeth", "Sami", "Anthony", "Romesh", "Kenneth", "Denise", "Bert", "Robert", "James", "Charles", "Joseph", "Janice", "Douglas", "Hendrik", "Mark", "Ronald", "Robert", "Daniel", "Charles", "Charles", "Fisk", "Curtis", "Helen", "Winifred", "Robert", "Mark", "Barry", "Ronald", "Gayle", "Thomas", "Fred", "Mark", "Dagmar", "Ronald", "Gwendolyn Sontheim", "Gary", "Kelcy", "Russ", "Margot", "John", "Nick", "Jack", "Mat", "Joseph", "Michael", "Neal", "Jeffrey", "Jeff", "Scott", "Jim", "Behdad", "Jose", "Ernest", "Marian", "Isaac", "Marc", "Ben", "Joseph", "Johnelle", "Dan", "Thai", "Bin", "Lynsi", "Peter", "Herbert", "Austen", "James", "John", "Rakesh", "Rupert", "Marianne", "Arturo", "Jay", "Donald", "Ty", "Hayes", "Jim", "Barry", "Thomas", "John", "Herbert", "Jeremy", "Travis", "Min", "Richard", "Gail", "Trevor", "Joseph", "Steven", "William", "Mary Alice", "Gabriel", "Joseph", "Richard", "Robert", "Bernard", "Thomas", "Elizabeth", "Richard", "Eric", "Martha", "Brad", "Eric", "Ross", "Jean", "Mark", "Steven", "Sid", "Charles", "Jim", "Pablo", "Daniel", "Anthony", "John", "James", "Stephen", "Peter", "Stephen", "Jay", "Jerry", "Vincent", "Daniel", "Jeffrey", "Hamilton", "Peter", "William", "Daniel", "Ira", "Richard", "Scott", "Jon", "Amos", "James", "Robert ", "John", "Bob", "William", "John", "Aerin", "Rodger", "David", "Rodney", "Steven", "Howard", "Thomas", "Jeffrey", "Carl", "Bennett", "David", "Lynn", "Herb", "Warren", "Donald", "Steve", "Jon", "Bill", "Nicolas", "Ronald", "William", "Sheldon", "Jonathan", "Frank", "Margaret", "George", "Todd", "James", "Stephen", "David", "John", "Penny", "Phillip", "Barbara", "Todd", "Norman", "Edward", "John Paul", "Kenneth", "Bom", "Steven", "Haim", "Daniel", "Thomas", "William", "Michael", "Eleanor", "Chris", "James", "Sean", "Stewart", "Hua", "Evan", "Charles", "Brian", "David", "William", "Reed", "Tomilson", "Drayton", "Dean", "Robert", "Richard", "Roger", "Chad", "Patricia", "Roger"]



def getNameData(query):
	driverpath ='driver/chromedriver'
	service = Service(driverpath)
	driver = webdriver.Chrome(service=service)

	url = f"https://www.behindthename.com/name/{query}"
	driver.get(url)

	# wait for the new content to be loaded
	sleep(2)

	# click to get the IPA transcription
	#driver.find_element(By.XPATH, "return toggle_pron").click()

	# Access the content of the page
	htmlPage = driver.page_source
	
	# if a folder with the name of the query doesn't exist, create it, then save the file
	if not os.path.isdir('nameHtmls'):
		os.mkdir('nameHtmls')
	with open(f"nameHtmls/{query}.html", 'w', encoding='utf-8') as output:
		output.write(htmlPage)
		
	# close the instance
	driver.close()

for n in names:
	getNameData(n)
