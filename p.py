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

import requests
from bs4 import BeautifulSoup
#use beautifulsoup to connect to the umsi website
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
#convert the html file for the website to one large string
html_str = soup.prettify(formatter=None)
#replace student with AMAZING student, change main photo, and add UMSI logos
html_str = html_str.replace('student', 'AMAZING student')
html_str = html_str.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg', '/Users/MatLefkofsky/Desktop/Junior/206/HW3/mat.png')
#html_str = html_str.replace('logo2.png', '/Users/MatLefkofsky/Desktop/Junior/206/HW3/logo.png')

f = open('try.html','w')
f.write(html_str)
f.close()