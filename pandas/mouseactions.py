from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/SunMoon Computer/Desktop/Automation/chromedriver.exe")
driver.get("http://www.doict.gov.bd/site/page/b9a1af8f-87b2-45f3-9fce-efc9159f8e1a/-#")
time.sleep(3)
odidoptor=driver.find_element_by_xpath("//*[@id='dawgdrops']/ul/li[2]/a")
time.sleep(2)
itihas=driver.find_element_by_xpath("//*[@id='dawgdrops']/ul/li[2]/div/div[1]/ul/li[1]/a")
time.sleep(2)
action=ActionChains(driver)
action.move_to_element(odidoptor).move_to_element( itihas).click().perform()

