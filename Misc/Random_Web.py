

import random
import pandas as pd
import webbrowser



#getting the lenght of the file
with open('top10milliondomains.csv', 'r') as f:
    lenght = sum(1 for line in f) - 1 # -1 for header


skip_rows = random.randint(0, lenght - 1) # we are going to skip this many lines 
# -1 is to not overshoot the last one   

df=pd.read_csv('top10milliondomains.csv',skiprows=skip_rows, nrows=1)

domain =df.iloc[0, 1] #to get the domain

webbrowser.open_new_tab(domain)



'''

if you absolutely need the freshest data uncomment this section and replace  the whole getting data part
its really inefficent and would probabily take you a few minutes and a few hundred mb of internet
Github says the CSV file is too big now I cant upload it. you can download it directly from the URL

url="https://www.domcop.com/files/top/top10milliondomains.csv.zip"

df=pd.read_csv(url)

domains=df['Domain']

Domain=random.coice(domains)

webbrowser.open_new_tab(domain)



'''