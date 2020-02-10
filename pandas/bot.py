import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
class Instragram:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.driver=webdriver.Chrome("C:/Users/SunMoon Computer/Desktop/Automation/chromedriver.exe")
        
    
    def close(self):
        self.driver.close()

    def login(self):
        driver=self.driver
        driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(2)
        driver.find_element_by_name("username").send_keys(self.username)
        driver.find_element_by_name("password").send_keys(self.password)
        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]").click()
        #driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
        #driver.switch_to_alert().accept()
        time.sleep(4)

        driver.get('https://www.instagram.com/p/B73hyWMnQT0/')
        driver.find_element_by_class_name("_8-yf5 ").click()
        time.sleep(4)
       

kanak=Instragram('kanakhassan3','kanakalhassan')
kanak.login()
