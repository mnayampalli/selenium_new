from selenium import webdriver
import time
import unittest
from POMDemo.Pages.LoginPage import LoginPage
from POMDemo.Pages.HomePage import HomePage

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome("C:/Users/Mahesh/PycharmProjects/selenium/drivers/chromedriver.exe")

        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        global driver
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        x=driver.title
        assert x=="abc"

        #self.driver.find_element_by_id("txtUsername").send_keys("Admin")

        #self.driver.find_element_by_id("txtPassword").send_keys("admin123")

        #self.driver.find_element_by_id("btnLogin").click()

        #self.driver.find_element_by_id("welcome").click()

        #self.driver.find_element_by_link_text("Logout").click()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):

        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")