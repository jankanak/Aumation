from selenium import webdriver
import re
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/SunMoon Computer/Desktop/Automation/chromedriver.exe")
driver.get("https://www.facebook.com/")
time.sleep(10)
search_input=driver.find_element_by_name('email')
search_input.send_keys('')

search_input=driver.find_element_by_name('pass')
search_input.send_keys('')
#print(search_input)
time.sleep(2)
search_button=driver.find_element_by_xpath("//*[@id='u_0_4']")
search_button.click()