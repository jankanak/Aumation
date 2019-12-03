from selenium import webdriver
import re
import time
import unittest
from selenium.webdriver.common.keys import Keys

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome("C:/Users/88015/Desktop/Automation/chromedriver.exe")
        cls.driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

    def test_login_test(self):
        self.driver.find_element_by_name("session_key").send_keys("kanakcsepust07@gmail.com")
        self.driver.find_element_by_id("password").send_keys("mashmsd6!")
        self.driver.find_element_by_xpath("//div[button/@class='btn__primary--large from__button--floating']").click()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()







