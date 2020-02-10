from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/SunMoon Computer/Desktop/Automation/chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.switch_to.frame(0)
driver.find_element_by_xpath("//*[@id='RESULT_FileUpload-10']").send_keys('E://kanak.jpg')
