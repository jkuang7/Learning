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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#Setting up the ChromeDriver for Selenium
# options = webdriver.ChromeOptions()
options = Options()
options.add_experimental_option('detach', True) #Keeps the chrome driver open after the script is finished
# options.add_experimental_option("detach", True) #disables the browser from being closed
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com")

print(driver.title) #prints the title of the page

#Finding elements
search_box = driver.find_element(By.CSS_SELECTOR, 'input').text
print(search_box)

#Finding elements by xpath
box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('giraffe')
box.send_keys(Keys.ENTER)

#Click on first link
box = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/a/h3')
box.click()

#Save screenshot
image = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[2]/td/a/img')
image.screenshot('giraffe.png')


#self scrolling
# while True:
#   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Waiting Strategies are required if we need to render element before we can interact with it
# driver.implicitly_wait(0.5)
#time.sleep(0.5)
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[2]/td/a/img')))
driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[2]/td/a/img').click()