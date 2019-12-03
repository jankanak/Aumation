from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/88015/Desktop/Automation/chromedriver.exe")
driver.get('http://wikipedia.org')
element=driver.find_element_by_tag_name('html')
element.send_keys(Keys.END)
time.sleep(4)
element.send_keys(Keys.HOME)