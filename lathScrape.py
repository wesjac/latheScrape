from bs4 import BeautifulSoup
import requests
from pick import pick

options = ['TH','Ross','Harp']

print(30*'-',"Lathe Scrape", 30*'-')

def menu_selector():
    title = 'Select a business: '
    option, index = pick(options, title)
    return option

def get_url(url):
	r = requests.get(url)
	r_html = r.text
	soup = BeautifulSoup(r_html)
	return soup

def print_lathe_pricelist(soup):
	l = [x.string for x in (soup.find_all(attrs = {'class':'list-group-item'}))]
	list = [str(x) for x in l]
	pricelist = [x.strip('None') for x in list]
	for y in pricelist:
		print(y)

choice = menu_selector()
print(choice)

if choice == 'TH':
    s = get_url('https://www.thmachinetools.co.za/products/used-machines/lathes')
    print_lathe_pricelist(s)
