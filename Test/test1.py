import time
from selenium import webdriver

driver = webdriver.Chrome("../drivers/chromedriver.exe")

driver.set_page_load_timeout(10)

driver.get("https://gmail.com")

time.sleep(3)

driver.find_element_by_id("identifierId").send_keys("disturbmahesh@gmail.com")

time.sleep(10)

driver.close()
driver.quit()

print("Test Completed")