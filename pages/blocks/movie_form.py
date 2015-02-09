from pages.page import Page
# from selenium.webdriver.support.select import Select


class MovieForm(Page):

    @property
    def movie_name_field(self):
        return self.driver.find_element_by_name("name")

    @property
    def movie_year_field(self):
        return self.driver.find_element_by_name("year")
