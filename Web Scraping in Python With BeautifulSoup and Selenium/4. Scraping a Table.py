#Grabbing data from world-population table -> df -> csv

import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml #lxml is a Python library for parsing HTML and XML documents

url = 'https://www.worldometers.info/world-population'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

tableHTML = soup.find(class_= 'table-striped');

headers = []
for th in tableHTML.find_all('th'): #Grab all the header cells of the table
  headers.append(th.text)

df = pd.DataFrame(columns=headers)

for tr in tableHTML.find_all('tr')[1:]: #Grab all the rows of the table after the header
    td_list = tr.find_all('td')
    td_str_list = [td.text for td in td_list]
    print(td_str_list)
    df.loc[len(df)] = td_str_list #append td_str_list to the dataframe -> len(df) grows in size as we append to it

print(df)
df.to_csv('Web Scraping in Python With BeautifulSoup and Selenium/test.csv');