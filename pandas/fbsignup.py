import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome("C:/Users/SunMoon Computer/Desktop/Automation/chromedriver.exe")
driver.get('https://www.facebook.com/')
time.sleep(5)
first_name=driver.find_element_by_id("u_0_m")
first_name.send_keys('lubu')
surname=driver.find_element_by_id('u_0_o')
surname.send_keys('sumu')
mobile=driver.find_element_by_xpath("//*[@id='u_0_r']")
mobile.send_keys('01521470683')
password=driver.find_element_by_id("u_0_w")
password.send_keys('lubusumu12')
##drop down
date=driver.find_element_by_name("birthday_day")
dropdate=Select(date)
dropdate.select_by_index(3)

year=driver.find_element_by_name("birthday_year")
dropdate=Select(year)
dropdate.select_by_visible_text("2001")

radiobutton=driver.find_element_by_name("sex")
radiobutton.click()
# signup=driver.find_element_by_id("u_0_13")
# signup.click()

