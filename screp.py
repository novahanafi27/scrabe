from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=opsi)

ecommerce_link = 'https://www.bukalapak.com/c/motor-471/motor?from=omnisearch&from_keyword_history=false&search_source=omnisearch_keyword&source=navbar'
driver.set_window_size(1300,800)
driver.get(ecommerce_link)
time.sleep(5)

driver.save_screenshot("home.png")
content = driver.page_source
driver.quit()

data = BeautifulSoup (content,'html.parser')

for area in data.find_all('div',class_=""):