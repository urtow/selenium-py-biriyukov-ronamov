from model.movie import Movie
from model.user import User
# from selenium_fixture import app


def test_add_movie(app):
    app.ensure_login_as(User.Admin())
    new_movie = Movie.the_movie()
    app.add_movie(new_movie)
    assert app.is_movie_added(new_movie)
