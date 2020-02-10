import pandas as pd
# df1=pd.DataFrame({
#      "name":["bd","au","en"],
#      "religion":["islam","christian","hindu"]
# })
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/SunMoon Computer/Desktop/Automation/chromedriver.exe")
driver.get('https://www.facebook.com/')
time.sleep(5)


df1=pd.read_excel('Book1.xlsx')
for name['name'] in df1.iterrows():
    first_name=driver.find_element_by_id("u_0_m")
    first_name.send_keys(name)

# df2=pd.DataF1rame({
#     "dept":["cse","eee","civil"],
#     "income":["120","45","12"]
# })
# df1=pd.read_excel('new1.xlsx')
# df2=pd.read_excel('output.xlsx')
# join=pd.concat([df1,df2],axis=1,keys=["country","dept"])
# join.to_excel('new2.xlsx')