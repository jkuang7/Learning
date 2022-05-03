#Scrape data from NFL Standings page for REG 2019 season

import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import lxml

url = 'https://www.nfl.com/standings/league/2019/REG'
soup = BeautifulSoup(requests.get(url).text, 'lxml') #not sure why soup isn't returning tags in order
print(soup)
table = soup.table

headers = []
for th in table.select('th'):
    headers.append(th.text)
    
print(headers)

df = pd.DataFrame(columns=headers)

for sup in table.select('sup'):
  sup.decompose() #Removes sup tag from the table tree so x, xz* in nfl_team_name will not show up

for tr in table.select('tr')[1:]:
    td_list = tr.select('td')
    td_str_list = [td_list[0].select('.d3-o-club-shortname')[0].text]
    td_str_list = td_str_list + [td.text for td in td_list[1:]]
    df.loc[len(df)] = td_str_list
    
print(df.to_string())