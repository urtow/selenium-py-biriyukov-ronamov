# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote("http://192.168.0.14:4444/wd/hub/", webdriver.DesiredCapabilities.FIREFOX)
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost/php4dvd"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get_screenshot_as_file("screen.png")
        driver.get(self.base_url + "/")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
