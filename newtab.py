from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/88015/Desktop/Automation/chromedriver.exe")
#driver=webdriver.Chrome()
driver.get("https://www.google.com")
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND+'t')
driver.get("https://www.bing.com")
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND+ 'W')
time.sleep(2)
#driver.close()
