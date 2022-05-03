#How to get the HTML
# find and final_all to scrape specific lines of HTML code that have data we want to scrape

import requests
from bs4 import BeautifulSoup
import pandas as pd

#Grabbing the URL
url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
page = requests.get(url)
page
soup = BeautifulSoup(page.text, 'lxml')
soup

#find
soup.find('header')
soup.header.attrs
soup.find('div', {'class':'container test-site'}) #similar to document query selector
soup.find('h4', {'class':'pull-right price'})
soup.find('h4', class_ = 'pull-right price') #class_ is a special variable that allows you to access the class attribute of an element -> same as above

#find_all - part 1 -> find_all returns a list of all that matches and then we can further index down via python syntax
soup.find_all('h4', {'class':'pull-right price'})[6:] #find all h4 tags with class pull-right price and only return the 6th element onwards
soup.find_all('a', class_ = 'title') #returns list of all a tags with class title
soup.find_all('p', class_ = 'pull-right')


#find_all - part 2
soup.find_all(['h4','p','a']) #returns list of all h4, p, and a tags

soup.find_all(id = True) #returns list of all tags with an id attribute

soup.find_all(string = 'Iphone') #returns list of textContents with the string Iphone in it -> You can apply len to see how many times it appears

import re #This module provides regular expression matching operations similar to those found in Perl.

soup.find_all(string = re.compile('Nok'))
soup.find_all(string = ['Iphone', 'Nokia 123'])
soup.find_all(class_ = re.compile('pull')) #returns list of all tags with class pull*
soup.find_all('p', class_ = re.compile('pull'))
soup.find_all('p', class_ = re.compile('pull'), limit = 3) #returns list of 3 p tags with class pull*
soup.find_all('a', {'href': re.compile(r'crummy\.com/')}) #r is a raw string to allow regex to be used so that special chararacters won't get interpreted into something else

#find_all - part 3 -> Parsing html elements for product details
product_name = soup.find_all('a', class_ = 'title')
product_name[0] #<a class="title" href="/test-sites/e-commerce/allinone/product/486" title="Nokia 123">Nokia 123</a>
print(product_name[0].text) #Nokia 123
price = soup.find_all('h4', class_ = 'pull-right price') #find all h4 tags with class pull-right price
price
reviews = soup.find_all('p', class_ = re.compile('pull'))
reviews
description = soup.find_all('p', class_ = 'description')
description

#Cleaning up HTML to get text content from all product details
product_name_list = []
for i in product_name:
    name = i.text
    product_name_list.append(name)


price_list = []
for i in price:
    price2 = i.text
    price_list.append(price2)


reviews_list = []
for i in reviews:
    reviews2 = i.text
    reviews_list.append(reviews2)


descriptions_list = []
for i in description:
    descriptions2 = i.text
    descriptions_list.append(descriptions2)

#pd dataFrames
table = pd.DataFrame({'Product Name':product_name_list, 'Description':descriptions_list,
                      'Price':price_list, 'Reviews':reviews_list})
print(table)


#extracted data from nested HTML tags
root = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')[6] #6th gallery item
print(root)
  
root.find('a').text #Name of product
root.find('p', class_ = 'description').text #Description of product
nav = soup.find_all('ul', class_ = 'nav', id = 'side-menu')[0]
nav.find_all('li')[1].text
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    










