import time
from selenium import webdriver

driver = webdriver.Chrome("../Drivers/chromedriver.exe")

driver.get("https://fb.com")

driver.find_element_by_css_selector("input.inputtext").send_keys("hello")

time.sleep(100)