# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


class TestAfterLoginApi():

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.driver.implicitly_wait(5)
        cls.base_url = "http://lamp.local/"
        cls.driver.get(cls.base_url)
        cls.accept_next_alert = True
        cls.driver.find_element_by_id("username").clear()
        cls.driver.find_element_by_id("username").send_keys("admin")
        cls.driver.find_element_by_name("password").clear()
        cls.driver.find_element_by_name("password").send_keys("admin")
        cls.driver.find_element_by_name("submit").click()

    def test_search_success(self):
        # Wait while we see all
        self.wait.until(visibility_of_element_located((By.ID, 'results')))
        driver = self.driver
        driver.get(self.base_url)
        movie_title = "yaya"
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys(movie_title)
        driver.find_element_by_id("q").send_keys(Keys.RETURN)
        assert self.is_movie_present(movie_title)

    def test_search_fail(self):
        driver = self.driver
        movie_title = "not found"
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys(movie_title)
        driver.find_element_by_id("q").send_keys(Keys.RETURN)
        assert self.no_search_results()

    def no_search_results(self):
        results = self.wait.until(visibility_of_element_located((By.ID, 'results')))
        message = results.find_element_by_class_name("content")
        if message.text == 'No movies where found.':
            return True
        else:
            return False
            return False

    def is_movie_present(self, movie_title):
        results = self.wait.until(visibility_of_element_located((By.ID, 'results')))
        movies_titles = results.find_elements_by_class_name("title")
        for title in movies_titles:
            if title.text == movie_title:
                return True
        return False

    @classmethod
    def teardown_class(cls):
        cls.driver.close()
