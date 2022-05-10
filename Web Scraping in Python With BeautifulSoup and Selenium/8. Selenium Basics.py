# Questions
# What is common by, support ui, and support?
# Why is time often imported?
# What is xpath? -- https://www.w3schools.com/xml/xpath_syntax.asp
# Why is xpath used as opposed to finding by name or id?
# Web Driver
# What are best principles for web scraping via xpath?

# https://selenium-python.readthedocs.io/locating-elements.html
# Write a script to google search giraffe and save the image to your computer
# Outcome: Write a script to save a screenshot of a div on a webpage by google searching it (and finding it in the results)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Setting up the ChromeDriver for Selenium
options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True) #disables the browser from being closed
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com")

print(driver.title) #prints the title of the page

#Waiting Strategies are required if we need to render element before we can interact with it
# driver.implicitly_wait(0.5)

#Finding elements
search_box = driver.find_element(By.CSS_SELECTOR, 'input').text
print(search_box)

#Finding elements by xpath
box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('giraffe')
