import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/SunMoon Computer/Desktop/Automation/chromedriver.exe")
driver.get("http://www.newtours.demoaut.com/")

link=driver.find_element_by_link_text("REGISTER").click()
link=driver.find_element_by_partial_link_text("S").click()
time.sleep(2)
driver.close()