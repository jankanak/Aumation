from selenium import webdriver
import re
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/88015/Desktop/Automation/chromedriver.exe")
driver.get("https://www.amazon.ca/")
time.sleep(10)
search_input=driver.find_element_by_id('twotabsearchtextbox')
search_input.send_keys('apple')

#print(search_input)
time.sleep(2)
search_button=driver.find_element_by_class_name("nav-input")
search_button.click()
