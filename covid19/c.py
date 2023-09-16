# Modules ; bs4 => (beautiful soup) pulling data out of HTML and XML files

# requests:  Requests allows you to send HTTP/1.1 requests extremely easily
 # Approach Extract data form given URL
""" Scrape the data with the help of requests and Beautiful Soup
Convert that data into html code.
Find the required details and filter them. """

""" These scripts will give you only Raw data in String """

import requests
from bs4 import BeautifulSoup

# URL get function create

def getdata(url):
	r = requests.get(url)
	return r.text

# Now pass the URL into the getdata function and Convert that data into HTML code

htmldata = getdata("https://covid-19tracker.milkeninstitute.org/")
soup = BeautifulSoup(htmldata, 'html.parser')
res = soup.find_all("div", class_="is_h5-2 is_developer w-richtext")
print(str(res))

""" COMPLETE CODE """

import requests
from bs4 import BeautifulSoup


def getdata(url):
	r = requests.get(url)
	return r.text

htmldata = getdata("https://covid-19tracker.milkeninstitute.org/")
soup = BeautifulSoup(htmldata, 'html.parser')
result = str(soup.find_all("div", class_="is_h5-2 is_developer w-richtext"))

print("NO 1 " + result[46:86])
print("NO 2 "+result[139:226])
print("NO 3 "+result[279:305])
print("NO 4 "+result[358:375])
print("NO 5 "+result[428:509])
