class Film:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating


class FilmLibrary:
    def __init__(self):
        self.films = {}

    def set_film(self, film):
        self.films[film.name] = film

    def get_film(self, name):
        return self.films[name]

    def get_films_info(self):
        return self.films