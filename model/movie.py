class Movie(object):

    def __init__(self, name="", year=""):
        self.name = name
        self.year = year

    @classmethod
    def the_movie(cls):
        return cls(name="TheMovie", year="2014")

    @classmethod
    def del_movie(cls):
        return cls(name="delete_me", year="2014")
