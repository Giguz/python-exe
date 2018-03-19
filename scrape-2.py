import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.google.it/search?q=bomboniere&oq=bomboniere&aqs=chrome..69i57j69i60j0l4.1850j0j1&sourceid=chrome&ie=UTF-8').text

soup = BeautifulSoup(source, 'lxml')
oksoup = soup.prettify()

mydivs = soup.findAll('p',class_='aw5cc')

for eachp in mydivs:
	print(eachp.text)