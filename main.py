from telebot import TeleBot
from film import FilmLibrary, Film

film_name = ''
film_rating = 0
films = dict()

bot = TeleBot('1015483974:AAFiuGMQB1CewhRP4JFbamvUZBjP9z3ytmw')
library = FilmLibrary()


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.from_user.id, 'Привет')


@bot.message_handler(commands='add')
def add(message):
    bot.send_message(message.from_user.id, 'Введите название фильма')
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    global film_name
    film_name = message.text
    bot.send_message(message.from_user.id, "Введите рейтинг фильма")
    bot.register_next_step_handler(message, get_film_rating)


def get_film_rating(message):
    global film_name
    global film_rating
    film_rating = int(message.text)
    library.set_film(Film(film_name, film_rating))
    bot.send_message(message.from_user.id, 'Рейтинг фильма успешно добавлен.')


@bot.message_handler(commands='list')
def get_film_list(message):
    a = ''
    for film in library.get_films_info():
        a += str(film)
        a += '\n'
    bot.send_message(message.from_user.id, a)


bot.polling()
