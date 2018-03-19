import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.google.it/search?q=bomboniere').text

soup = BeautifulSoup(source, 'lxml')
oksoup = soup.prettify()

mydivs = soup.findAll('p',class_='aw5cc')

for eachp in mydivs:
	print(eachp.text)