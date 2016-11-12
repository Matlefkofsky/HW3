# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import webbrowser
import re

base_url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
r = requests.get(base_url) 
soup = BeautifulSoup(r.text, "html.parser") #using beautiful soup to scrape the HTML from the website

for each in soup.find_all(text = re.compile("student")): 
	x = str(each)
	x = x.replace("student", "AMAZING student") #Replaces student with Amazing Student each time
	each.replaceWith(x)

for image in soup.find_all('img'):
	if image['src'] == "https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg": #finds image to replace
		image['src'] = "Mat.png" #grabs my image
	else:
		image['src'] = "Media/logo.png" #goes into media folder and grabs new logo and replaces it

my_string = str(soup)


txtfile = open("my_website.html", "w")
txtfile.write(str(soup)) #writes the new file
txtfile.close()