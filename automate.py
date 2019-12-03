from selenium import webdriver
import re
driver=webdriver.Chrome("C:/Users/88015/Desktop/Automation/chromedriver.exe")
driver.get('http://www.onecore.net')
na=driver.find_elements_by_xpath("//*[@id]")
for ii in na:
    print(ii.get_attribute('id'))


#("//form[@id='loginForm']")
