from bs4 import BeautifulSoup
import lxml
import requests #HTTP library to send HTTP/1.1 requests

# Basics of BeautifulSoup
# Acquiring HTML of web page via Python
# Components -- Tag, NavigableString, Strings, Attributes, Comments

#Acquiring HTML of web page
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
page = requests.get(url) #Returns Response Object

soup = BeautifulSoup(page.text, 'lxml')

#Tags
soup.header
soup.div

#NaviagableString
tag = soup.header.p
tag #returns p in HTML
tag.string #returns textContent of p

#Attributes - id, class, src, style, href, alt, title, data-*
tag = soup.header.a
tag #returns a in HTML
tag.attrs #returns attributes dict of a
# print(tag.attrs) #{'data-toggle': 'collapse-side', 'data-target': '.side-collapse', 'data-target-2': '.side-collapse-container'}
# print(tag.attrs['data-toggle'])
tag['attribute_new'] = 'this is a new attribute' #adds new attribute

#Comments
