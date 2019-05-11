import time
from selenium import webdriver

driver = webdriver.Chrome("../Drivers/chromedriver.exe")

driver.get("https://rediff.com")

#using link text as css... partial values
driver.find_element_by_css_selector("a[title*='Sign in']").click()
time.sleep(2)

#driver.find_element_by_xpath("a[contains(title,'Sign in')]").click()
#time.sleep(2)

driver.find_element_by_xpath("//input[@id='login1']").send_keys("namaskara")
time.sleep(2)

driver.find_element_by_css_selector("input#password").send_keys("namaskara")
time.sleep(2)

driver.find_element_by_xpath("//input[contains(@name,'proc')]").click()
time.sleep(2)

time.sleep(100)