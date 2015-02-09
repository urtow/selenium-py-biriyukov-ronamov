from internal_page import InternalPage
from pages.blocks.movie_form import MovieForm


class AddMoviePage(InternalPage):

    def __init__(self, driver, base_url):
        super(AddMoviePage, self).__init__(driver, base_url)
        self.movie_form = MovieForm(self.driver, self.base_url)

    @property
    def save_button(self):
        return self.driver.find_element_by_css_selector("img[alt=\"Save\"]")
