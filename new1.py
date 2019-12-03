from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://google.com")
driver.get("https://www.google.com")
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND+'t')
driver.get("https://www.bing.com")
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+ 'W')
time.sleep(2)