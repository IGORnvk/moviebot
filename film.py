class Film:
    def __init__(self, name, rating, favourite=False):
        self.name = name
        self.rating = rating
        self.favourite = favourite

    def __str__(self):
        return "Фильм: %s, рейтинг: %d" % (self.name, self.rating)

    @staticmethod
    def str_to_film(s):
        properties = s.split(' ')
        return Film(properties[0], int(properties[1]))




class FilmLibrary:
    def __init__(self):
        self.films = dict()

    def set_film(self, film):
        self.films[film.name] = film
        self.add_film_to_file(film)

    def get_film(self, name):
        return self.films[name]

    def get_films_info(self):
        return list(self.films.values())

    def del_film(self, name):
        del self.films[name]

    def read_films_from_file(self):
        f = open('film list', 'r')
        data = f.read()
        if data == '':
            return
        li = data.split('\n')
        li.pop()
        film_list = list(map(Film.str_to_film, li))
        for film in film_list:
            self.set_film(film)

    def add_film_to_file(self, film):
        f = open('film list', 'a')
        f.write(film.name + ' ' + str(film.rating) + '\n')
        f.close()

    def get_favourite_list(self):
        li = []
        for film in self.get_films_info():
            if film.favourite:
                li.append(film)
        return li

    def set_favourite(self, film_name):
        self.films[film_name].favourite = True
