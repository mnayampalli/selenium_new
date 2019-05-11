import time
from selenium import webdriver

driver = webdriver.Chrome("../Drivers/chromedriver.exe")

driver.set_page_load_timeout(10)

driver.get("https://gmail.com")

driver.find_element_by_id("identifierId").send_keys("disturbmahesh@gmail.com")

driver.find_element_by_class_name("CwaK9").click()

time.sleep(2)

driver.find_element_by_name("password").send_keys("Mahe!1904")

time.sleep(100)

driver.find_element_by_class_name("CwaK9").click()

time.sleep(100)

#driver.find_element_by_class("gb_b gb_hb gb_R").click()

#time.sleep(2)

#driver.find_element_by_id("gb_71").click()

#driver.close()

#driver.quit()

print("Test Completed")