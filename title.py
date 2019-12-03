from selenium import webdriver
driver=webdriver.Chrome("C:/Users/88015/Desktop/Automation/chromedriver.exe")
driver.get('http://google.com')

try:
    assert "Google" in driver.title
    print("it is ok that google is in their  title")
except Exception as  e:
    print("exception is found",format(e))

