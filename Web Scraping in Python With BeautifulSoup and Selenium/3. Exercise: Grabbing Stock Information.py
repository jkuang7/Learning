#https://marketwatch.com/investing/stock/aapl

#Grab the price of the stock
#Grab the closing price of the stock
#Grab the 52 week range of the stock
#Grab Analyst Ratings

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://marketwatch.com/investing/stock/aapl'
page = requests.get(url)
page
soup = BeautifulSoup(page.text, 'lxml')

#Grab price
price = soup.find('h2', class_ = 'intraday__price').find('bg-quote').text


#Grab closing price
closing_price = soup.find(class_ = 'u-semi').text

#Grab 52 week range -- Nested HTML with same tags everywhere
root = soup.find_all('mw-rangebar')[2]
low = root.find(class_ = 'primary').text
high = root.find_all(class_ = 'primary')[1].text

#Grab Analyst Ratings
active_rating = soup.find(class_='analyst__option active').text

print(low, high)
print(price)
print(closing_price)
print(active_rating)