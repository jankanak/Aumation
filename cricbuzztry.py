from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/88015/Desktop/Automation/chromedriver.exe")
driver.get('http://www.cricbuzz.com')
cla=driver.find_element_by_link_text('All Matches')
# for class_name in cla:
#     print(class_name.get_attribute('class'))

driver.implicitly_wait(3)
cla.click()
time.sleep(2)
driver.refresh()
time.sleep(3)
driver.back()
time.sleep(6)
driver.forward()

#driver.close()
