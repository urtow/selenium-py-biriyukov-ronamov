# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://lamp.local/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled(self):
        driver = self.driver
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
