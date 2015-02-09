from internal_page import InternalPage


class MoviePage(InternalPage):

    @property
    def movie_title(self):
        return self.driver.find_element_by_id("movie").text.rstrip()
