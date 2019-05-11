import time
from selenium import webdriver

driver = webdriver.Chrome("../Drivers/chromedriver.exe")

driver.get("https://fb.com")

driver.find_element_by_name("email").send_keys("hello")

time.sleep(2)

driver.find_element_by_id("pass").send_keys("namaskara")

time.sleep(2)

driver.find_element_by_id("u_0_j").send_keys("Mahesh")

time.sleep(2)

driver.find_element_by_xpath("//*[@id='u_0_l']").send_keys("Nayampalli")

time.sleep(2)

driver.find_element_by_css_selector("#u_0_o").send_keys("hello@gmail.com")

time.sleep(2)

driver.find_element_by_name("reg_email_confirmation__").send_keys("hello@gmail.com")

time.sleep(2)

driver.find_element_by_xpath("//input[@name='reg_passwd__']").send_keys("vanakkam")

time.sleep(2)

driver.find_element_by_id("day").send_keys("24")

time.sleep(2)

driver.find_element_by_id("month").send_keys("May")

time.sleep(2)

driver.find_element_by_id("year").send_keys("1990")

time.sleep(2)

driver.find_element_by_xpath("//input[@id='u_0_a']").click()

time.sleep(2)

driver.find_element_by_link_text("Forgotten account?").click()

time.sleep(2)

driver.find_element_by_css_selector("input[type='text']").send_keys("8105512005")

#salesforce
#driver.find_element_by_xpath("//input[@type='email']").send_keys("hello")
#driver.find_element_by_css_selector("input[type='email']").send_keys("hello")
#driver.find_element_by_css_selector("input#username").send_keys("hello")
#driver.find_element_by_css_selector("input#username").send_keys("hello")
time.sleep(100)

print("Test Completed")