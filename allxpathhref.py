import time 
from selenium import webdriver
driver=webdriver.Chrome("C:/Users/88015/Desktop/Automation/chromedriver.exe")
driver.get('http://www.onecore.net')
href=driver.find_elements_by_xpath("//*[@href]")
for link in href:
     print(link.get_attribute('href'))

driver.close()