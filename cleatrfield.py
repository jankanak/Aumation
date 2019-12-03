import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/88015/Desktop/Automation/chromedriver.exe")
driver.get('http://www.google.com')
#serach=driver.find_element_by_id("lst-ib")
search=driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
search.send_keys("python")
search.send_keys(Keys.RETURN)
driver.close()