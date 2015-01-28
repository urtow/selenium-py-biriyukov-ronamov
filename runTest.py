# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException


class TestApi():

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)
        cls.base_url = "http://lamp.local/"
        cls.driver.get(cls.base_url)
        cls.accept_next_alert = True
        cls.driver.find_element_by_id("username").clear()
        cls.driver.find_element_by_id("username").send_keys("admin")
        cls.driver.find_element_by_name("password").clear()
        cls.driver.find_element_by_name("password").send_keys("admin")
        cls.driver.find_element_by_name("submit").click()

    def test_add_movie_all_req_fields(self):
        driver = self.driver
        movie_title = 'Ya_ya_ya_ya'
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(movie_title)
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("2011")
        driver.find_element_by_id("submit").click()
        self.driver.get(self.base_url)
        assert self.is_movie_present(movie_title)

    def test_add_movie_not_all_req_fields(self):
        driver = self.driver
        movie_title = 'no-no-no-no'
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(movie_title)
        driver.find_element_by_id("submit").click()
        self.driver.get(self.base_url)
        assert not self.is_movie_present(movie_title)

    def test_delete_movie(self):
        movie_title = "delete_me"
        try:
            result = self.driver.find_element_by_id('results')
            movies_titles = result.find_elements_by_class_name("title")
            for title in movies_titles:
                if title.text == movie_title:
                    title.click()
                    self.driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
                    self.driver.switch_to_alert().accept()
                    assert not self.is_movie_present(movie_title)
                else:
                    assert False
        except NoSuchElementException:
            assert False

    def is_movie_present(self, movie_title):
        try:
            result = self.driver.find_element_by_id('results')
            movies_titles = result.find_elements_by_class_name("title")
            for title in movies_titles:
                if title.text == movie_title:
                    return True
        except NoSuchElementException:
            return False

    @classmethod
    def teardown_class(cls):
        cls.driver.close()
