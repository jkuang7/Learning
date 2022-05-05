# Grab link, name, price, color of each car -> do first 10-15 pages

import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

url = 'https://www.carpages.ca/used-cars/search/?category_id=2';
soup = BeautifulSoup(requests.get(url).text, 'lxml')

df = pd.DataFrame({'Link': [''], 'Name': [''], 'Price': [''], 'Color': ['']})

for i in range(1, 16):
  posts = soup.select('.media')
  for post in posts:
    link = 'https://www.carpages.ca/' + post.select_one('a').get('href')
    name = post.select_one('a').get('title').strip()
    price = post.select_one('.delta ').text.strip()
    color = post.select_one('[class="l-row soft-half--top"] div:nth-child(3) span').text.strip()
    df = df.append({'Link': link, 'Name': name, 'Price': price, 'Color': color}, ignore_index=True)
  try:
    next_page = soup.select_one('.nextprev').get('href')
    soup = BeautifulSoup(requests.get(next_page).text, 'lxml')
  except:
    pass
print(df.to_string())