import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

    def like_photo(self,hashtag):
        driver=self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(3)
        for i in range(1,2):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(2)
        hrefs=driver.find_elements_by_tag_name("a")
        pic_hrefs=[elem.get_attribute('href') for elem in hrefs]
        print(len(pic_hrefs))
        # pic_hrefs=[href for href in pic_hrefs if hashtag in href]
        # print(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            try:
                driver.find_element_by_class_name('_8-yf5').click()
                time.sleep(15)
            except Exception as e:
                time.sleep(2)

kanak=Instragram('kanakhassan3','kanakalhassan')
kanak.login()
kanak.like_photo('newyork')