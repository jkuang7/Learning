#Scrape data from NFL Standings page for REG 2019 season
#Note: soup is grabbing the tags in order of the original HTML response but the table is rendering dynamically based on the sort order of the table

import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

url = 'https://www.nfl.com/standings/league/2019/REG'
soup = BeautifulSoup(requests.get(url).text, 'lxml')
table = soup.table

# someTable = pd.read_html('https://www.nfl.com/standings/league/2019/REG')[0].sort_values(by='PCT',ascending=False)
# print(someTable.to_string())

headers = []
for th in table.select('th'):
    headers.append(th.text)

df = pd.DataFrame(columns=headers)

for sup in table.select('sup'):
  sup.decompose() #Removes sup tag from the table tree so x, xz* in nfl_team_name will not show up

for tr in table.select('tr')[1:]:
    td_list = tr.select('td')
    td_str_list = [td_list[0].select('.d3-o-club-shortname')[0].text]
    td_str_list = td_str_list + [td.text for td in td_list[1:]]
    df.loc[len(df)] = td_str_list

# print(df.to_string()) #Original Order
print(df.sort_values(by='PCT', ascending=False).to_string()) #sort by PCT