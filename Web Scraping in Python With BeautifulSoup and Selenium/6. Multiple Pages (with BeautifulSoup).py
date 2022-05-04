# Summary: We want to grab content from multiple pages but BeautifulSoup does not support clicking. We'll make requests for the next page by grabbing the href attribute from the next page btn instead

# Grab the roots from the galleryView
# For each root
  # try
    # Grab the information we need
    # Append the information to df
  # except -> we may not get a valid element in one of the posts
    # pass (ignore)
# Grab the next page url
# Make a new request
# Update soup

import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

url = 'https://www.airbnb.ca/s/Las-Vegas--Nevada--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Las%20Vegas%2C%20NV%2C%20USA&source=structured_search_input_header&search_type=autocomplete_click&place_id=ChIJ0X31pIK3voARo3mz1ebVzDo&federated_search_session_id=ce805a2e-de71-44a7-aa20-19e564d7e6e5&pagination_search=true&items_offset=280&section_offset=4' #Test last page to reduce test time

url = 'https://www.airbnb.ca/s/Las-Vegas--Nevada--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Las%20Vegas%2C%20Nevada%2C%20United%20States&source=structured_search_input_header&search_type=autocomplete_click&place_id=ChIJ0X31pIK3voARo3mz1ebVzDo'

soup = BeautifulSoup(requests.get(url).text, 'lxml') #the raw html from requests is not necessirally organized the way it would match on a webpage

# if the web page is rendering data dynamically, we can write the raw html to a file, load it, stop the page for parsing reasons, and then query the data we need
with open("output.html", "w") as file:
    file.write(str(soup))

#tip: use break statements to test for single posts -> Build logic upwards

df = pd.DataFrame({'Link': [''], 'Title': [''], 'Rating': [''], 'Description': ['']})

while True:
  posts = soup.select('._1e9w8hic')
  for post in posts:
    link = post.select_one('a').get('href')
    link_full = 'https://www.airbnb.ca/' + link
    title = post.select_one('[itemprop="name"]').get('content')
    desc = post.select_one('.mj1p6c8').text
    rating = post.select_one('span[aria-label] span[aria-hidden="true"]').text
    df = df.append({'Link': link_full, 'Title': title, 'Rating': rating, 'Description': desc}, ignore_index=True)

  
  next_page = soup.select_one('a[aria-label="Next"]')
  if next_page:
    next_page_url = 'https://www.airbnb.ca/' + next_page.get('href')
    soup = BeautifulSoup(requests.get(next_page_url).text, 'lxml')
  else:
    break
# df.sort_values(by=['Rating'], inplace=True, ascending=False)
print(df.to_string())