
#idea is simple

#extract random quotes and summaries of wikipedia from APIs,each time randomized

#down the line add a web scraper for additional functionality

#prompt an AI for info to add to the pool

#pool those strings to an array

#select a random string from the array, print to an output 



import requests

import random


#adviceslip

adviceslip_response= requests.get("https://api.adviceslip.com/advice")
adviceslip_data=adviceslip_response.json()
final_slip=adviceslip_data["slip"]["advice"]



#zenquotes

zenquotes_response= requests.get("https://zenquotes.io/api/random")
zenquotes_data=zenquotes_response.json()
final_zen=zenquotes_data[0]["q"]

#stoicquotes



stoic_response= requests.get("https://stoic-quotes.com/api/quote")
stoic_data=stoic_response.json()
final_stoic=stoic_data["text"]

#quotable

import urllib3
urllib3.disable_warnings()
quotable_response=requests.get("https://api.quotable.io/quotes/random",verify=False,timeout=10)
quotable_data=quotable_response.json()
final_quotable=quotable_data[0]["content"]

#vercel

vercel_response= requests.get("https://qapi.vercel.app/api/random")
vercel_data=vercel_response.json()
final_vercel=vercel_data["quote"]



#Wikipedia


import wikipedia

try:


  Wiki_title=wikipedia.random()
  Wiki_summary=wikipedia.summary(Wiki_title,auto_suggest=True,redirect=True)


  #print(Wiki_summary)

except:
	print("wikipedia disambiguation error, run the code again")
	
"""

# an interesting fact from deepseek AI



model_id="deepseek-ai/DeepSeek-R1"
AI_API_URL ="https://api-inference.huggingface.com/models/deepseek-ai/DeepSeek-R1"
AI_API_KEY="YOUR_API_KEY"
headers = {
"Authorization":f"Bearer {AI_API_KEY}  " ,
"x-use-cache": 'true',
"Content-Type": "application/json"
}

AI_prompt=" give me an interesting fact"

AI_payload = {
    "inputs": f"{AI_prompt}",
}

AI_response = requests.post(AI_API_URL, headers=headers, json=AI_payload)

AI_response_f=AI_response.text

"""



#ninja fact

ninja_fact_url = 'https://api.api-ninjas.com/v1/facts'
ninja_fact_key="Ninja_fact_key"

headers={
'X-Api-Key': f'{ninja_fact_key}'
}

ninja_response = requests.get(ninja_fact_url , headers=headers)
ninja_response_content=ninja_response.json()
final_ninja_fact=ninja_response_content[0]["fact"]


#random useless fact


useless_url='https://uselessfacts.jsph.pl/random.json'

useless_response=requests.get(useless_url)
useless_json=useless_response.json()

useless_final=useless_json["text"]

#scrape wikipedia



import requests
from bs4 import BeautifulSoup
import html


#the url of the site of the site you are scraping
scrape_url="https://en.m.wikipedia.org/wiki/Main_Page"

scrape_page=requests.get(scrape_url)

scrape_soup=BeautifulSoup(scrape_page.content,"html.parser")


#configure this part to get which element you want
mp_tfa = scrape_soup.find('div', id='mp-tfa')
all_scrape_quote= mp_tfa.find_all('p')


scrape_quotes=[]

for tx in all_scrape_quote:
	clean_text=html.unescape(tx.get_text())
	scrape_quotes.append(clean_text)


final_scrape_quote=scrape_quotes[0]
#print(final_scrape_quote)






#these are the things I'm getting




shared_pool=[final_slip,final_zen,final_stoic,final_quotable,final_vercel,Wiki_summary,useless_final,final_ninja_fact,AI_response_f]

#print(shared_pool)

Final_Result=random.choices(shared_pool)
print(Final_Result)





  