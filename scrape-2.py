import requests
import csv
from bs4 import BeautifulSoup

csv_file = open('ric_correlate.csv','w')
csv_writer = csv.writer(csv_file)



source = requests.get('https://www.google.it/search?q=bomboniere').text
soup = BeautifulSoup(source, 'lxml')

mydivs = soup.findAll('p',class_='aw5cc')

for eachp in mydivs:
	print("https://www.google.it" + eachp.a['href'])
	csv_writer.writerow([eachp.text])


csv_file.close()

def gotourl(url):
	newurl = requests.get('url').text
	return newurl

# def listurl(url):
# 	source = requests.get('https://www.google.it/search?q=bomboniere').text
# 	soup = BeautifulSoup(source, 'lxml')

# 	mydivs = soup.findAll('p',class_='aw5cc')

# 	for eachp in mydivs:
# 		print(eachp)
	