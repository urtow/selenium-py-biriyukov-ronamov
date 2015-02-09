from pages.page import Page
from selenium.webdriver.common.by import By


class InternalPage(Page):

    @property
    def logout_button(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?logout']")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "nav"))

    @property
    def add_movie_link(self):
        return self.driver.find_element_by_css_selector("img[alt=\"Add movie\"]")

    @property
    def search_field(self):
        return self.driver.find_element_by_id("q")
