import requests
import csv
from bs4 import BeautifulSoup



def getkw(url):
	source = requests.get(url).text
	soup = BeautifulSoup(source, 'lxml')

	mydivs = soup.findAll('p',class_='aw5cc')

	for eachp in mydivs:
		return eachp



def gethttp(url):
	source = requests.get(url).text
	soup = BeautifulSoup(source, 'lxml')
	mydivs = soup.findAll('p',class_='aw5cc')

	for eachp in mydivs:
		print("https://www.google.it" + eachp.a['href'])
		

def gotourl(url):
	newurl = requests.get('url').text
	return newurl

# def listurl(url):
# 	source = requests.get('url').text
# 	soup = BeautifulSoup(source, 'lxml')

# 	mydivs = soup.findAll('p',class_='aw5cc')

# 	for eachp in mydivs:
# 		print(eachp)
# csv_file = open('ric_correlate.csv','w')
# csv_writer = csv.writer(csv_file)

#csv_writer.writerow([eachp.text])
#csv_file.close()
#
	
getkw("https://www.google.it/search?q=bomboniere")		
gethttp('https://www.google.it/search?q=bomboniere')

