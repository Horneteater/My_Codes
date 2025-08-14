


import requests
from bs4 import BeautifulSoup
import html


#the url of the site of the site you are scraping
scrape_url="https://en.m.wikipedia.org/wiki/Main_Page"

scrape_page=requests.get(scrape_url)

scrape_soup=BeautifulSoup(scrape_page.content,"html.parser")


#configure this part to get which element you want
#all_scrape_quote=scrape_soup.find('div', id='mp-tfa')
mp_tfa = scrape_soup.find('div', id='mp-tfa')
all_scrape_quote= mp_tfa.find_all('p')


scrape_quotes=[]

for tx in all_scrape_quote:
	clean_text=html.unescape(tx.get_text())
	scrape_quotes.append(clean_text)


#print(scrape_quotes)

final_scrape_quote=scrape_quotes[0]
print(final_scrape_quote)