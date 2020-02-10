import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/SunMoon Computer/Desktop/Automation/chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")

popup=driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
driver.switch_to_alert().accept()
time.sleep(2)

popup1=driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
driver.switch_to_alert().dismiss()
