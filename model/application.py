from model.user import User
from pages.internal_page import InternalPage
from pages.login_page import LoginPage
from pages.add_movie_page import AddMoviePage
from pages.movie_page import MoviePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present, presence_of_element_located


class Application(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 10)
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.add_movie_page = AddMoviePage(driver, base_url)
        self.movie_page = MoviePage(driver, base_url)

    def logout(self):
        self.internal_page.logout_button.click()
        self.wait.until(alert_is_present()).accept()

    def ensure_logout(self):
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        if element.tag_name == "nav":
            self.logout()

    def login(self, user):
        lp = self.login_page
        lp.is_this_page
        lp.username_field.send_keys(user.username)
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def ensure_login_as(self, user):
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        if element.tag_name == "nav":
            # we are on internal page
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user)

    def is_logged_in(self):
        return self.internal_page.is_this_page

    def is_logged_in_as(self, user):
        return self.is_logged_in() \
            and self.get_logged_user().username == user.username

    def is_not_logged_in(self):
        return self.login_page.is_this_page

    def get_logged_user(self):
        self.internal_page.user_profile_link.click()
        upp = self.user_profile_page
        upp.is_this_page
        return User(username=upp.user_form.username_field.get_attribute("value"),
                    email=upp.user_form.email_field.get_attribute("value"))

    def add_movie(self, movie):
        self.internal_page.add_movie_link.click()
        amp = self.add_movie_page
        amp.movie_form.movie_name_field.send_keys(movie.name)
        amp.movie_form.movie_year_field.send_keys(movie.year)
        amp.save_button.click()

    def is_movie_added(self, movie):
        amp = self.movie_page
        expected_title = movie.name + " (" + movie.year + ")\nDVD"
        if amp.movie_title == expected_title:
            return True
        else:
            return False

    def delete_movie(self, movie):

