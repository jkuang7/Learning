from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

#Starts the driver and goes to our starting webpage
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://store.unionlosangeles.com/collections/outerwear')

#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if last_height == new_height:
        break
    last_height = new_height
    
from bs4 import BeautifulSoup
import pandas as pd

# #Download HTML of the webpage -> Open HTML and parse it -> use BeautifulSoup to grab the data -> Faster way of testing
# with open("output.html", "w") as file:
#     file.write(str(soup))

# #Open the HTML file and parse it
# with open("output.html", "r") as file:
#   soup = BeautifulSoup(file, 'lxml')

# #Imports the HTML of the selenium webpage and parses it (connecting selenium to BeautifulSoup)
soup = BeautifulSoup(driver.page_source, 'lxml')

#Creates a dataframe
df = pd.DataFrame({'Link':[''], 'Vendor':[''],'Title':[''], 'Price':['']})

#Store in an array with all products -> Returns an array with one section
# section = soup.select('#isp_search_results_container')

#Grab the container HTML with all the products
section = soup.find(id = 'isp_search_results_container')

#Find all the products in the section
postings = section.find_all(class_ = 'isp_grid_product')

#Grabs the product details for every product on the page and adds each product as a row in our dataframe
for post in postings:
    try:
        link = 'https://store.unionlosangeles.com/' + post.find('a').get('href')
        vendor = post.find(class_= 'isp_product_vendor').text
        title = post.find(class_ = 'isp_product_title').text
        price = post.find(class_ = 'isp_product_price money').text
        df = df.append({'Link':link, 'Vendor':vendor,'Title':title, 'Price':price}, ignore_index = True)
    except:
        pass

print(df.to_string())