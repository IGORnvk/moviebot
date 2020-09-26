class Film:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __str__(self):
        return "film: %s, rating: %d" % (self.name, self.rating)

class FilmLibrary:
    def __init__(self):
        self.films = dict()

    def set_film(self, film):
        self.films[film.name] = film

    def get_film(self, name):
        return self.films[name]

    def get_films_info(self):
        return list(self.films.values())

    def del_film(self, name):
        del self.films[name]