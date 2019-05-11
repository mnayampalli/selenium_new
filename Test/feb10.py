import time
from selenium import webdriver

driver = webdriver.Chrome("../Drivers/chromedriver.exe")

driver.get("https://fb.com")

#Error message for compound class:
#driver.find_element_by_class_name("inputtext _58mg _5dba _2ph-").send_keys("Mahesh")
#Message: invalid selector: Compound class names not permitted

driver.find_element_by_name("firstname").send_keys("Mahesh")

time.sleep(2)

driver.find_element_by_name("lastname").send_keys("Acharya")

time.sleep(2)

driver.find_element_by_name("reg_email__").send_keys("disturbmahesh@gmail.com")

time.sleep(2)

driver.find_element_by_name("reg_email_confirmation__").send_keys("disturbmahesh@gmail.com")

time.sleep(2)

driver.find_element_by_name("reg_passwd__").send_keys("GoodMorning@123")

time.sleep(2)

driver.find_element_by_name("birthday_day").send_keys("24")

time.sleep(2)

driver.find_element_by_name("birthday_month").send_keys("May")

time.sleep(2)

driver.find_element_by_name("birthday_year").send_keys("1990")

time.sleep(2)

#driver.find_element_by_xpath("//*[@id='u_0_9']").click()

#time.sleep(2)

driver.find_element_by_css_selector("input#u_0_9").click()

time.sleep(2)

#driver.find_element_by_name("pass").send_keys("Mahe!5670")

#driver.find_element_by_link_text("Forgotten account?").click()

time.sleep(100)