import time
from selenium import webdriver

driver = webdriver.Chrome("../Drivers/chromedriver.exe")

driver.get("https://google.com")

driver.find_element_by_xpath("//div[@class='a4bIc']/input").send_keys("Welcome to automation")

time.sleep(100)