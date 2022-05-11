# Open in google chrome -> top 100 movies of all time
# https://www.imdb.com/chart/top
# create a waittime -> self-scroll all the way down to 50th best movie of all time
# click on the movie -> grab the image

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Starts our driver and goes to the starting webpage which is google.com
options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com")

driver.get('https://google.com')

#Inputs text into the google search box
box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('top 100 movies of all time imdb')

#Presses the enter button to search
box.send_keys(Keys.ENTER)
time.sleep(2)

#Presses on the link for Imdb
press = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div[1]/div/a/h3').click()

#3 second wait time to let the entire page load in
time.sleep(2)

#Scrolls until Jaws the movie is on the screen
driver.execute_script('window.scrollTo(0,22500)')

#Takes a screenshot of the webpage
driver.save_screenshot('50.png')

#Takes a screenshot of the Jaws movie poster
driver.find_element(By.CSS_SELECTOR, '#main > div > div.lister.list.detail.sub-list > div > div:nth-child(50) > div.lister-item-image.float-left > a > img').screenshot('50_1.png')



