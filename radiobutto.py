from selenium import webdriver
import time
from selenium.webdriver.common.keys import  Keys
driver=webdriver.Chrome("C:/Users/88015/Desktop/Automation/chromedriver.exe")
driver.get('https://www.ironspider.ca/forms/checkradio.htm')
driver.find_element_by_xpath("//form/input[1]").click()
#driver.find_element_by_name("//*[contains(text(),' Red')]").click()
# for i in driver.find_elements_by_name("color"):
#     i.click()
#     time.sleep(2)
# time.sleep(6)
# driver.close()
