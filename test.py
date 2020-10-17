import film

film_library = film.FilmLibrary()
film_1 = film.Film('abc', 1)
film_2 = film.Film("dfg", 9)

film_library.set_film(film_1)
film_library.set_film(film_2)

film_library.del_film(film_1.name)

film_library.read_films_from_file()

film_list = film_library.get_films_info()

for film in film_list:
    print(film)

