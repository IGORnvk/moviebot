from telebot import TeleBot
from film import FilmLibrary, Film
from telebot import types

film_name = ''
film_rating = 0
films = dict()

help_text = '/start \n /add \n /list \n /add_fav \n /fav \n'
bot = TeleBot('1015483974:AAFiuGMQB1CewhRP4JFbamvUZBjP9z3ytmw')
library = FilmLibrary()
library.read_films_from_file()


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Список всех команд:' '\n' + help_text)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.from_user.id, 'Привет')


@bot.message_handler(commands=['add'])
def add(message):
    bot.send_message(message.from_user.id, 'Введите название фильма')
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    global film_name
    film_name = message.text
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row('1', '2')
    markup.row('3', '4')
    markup.row('5','6')
    markup.row('7', '8')
    markup.row('9', '10')
    msg = bot.send_message(message.from_user.id, 'Введите рейтинг фильма', reply_markup=markup)
    bot.register_next_step_handler(message, get_film_rating)


def get_film_rating(message):
    global film_name
    global film_rating
    film_rating = int(message.text)
    library.set_film(Film(film_name, film_rating))
    bot.send_message(message.from_user.id, 'Рейтинг фильма успешно добавлен.')


@bot.message_handler(commands=['list'])
def get_film_list(message):
    a = ''
    for film in library.get_films_info():
        a += str(film)
        a += '\n'
    bot.send_message(message.from_user.id, a)


@bot.message_handler(commands=['fav'])
def favourites(message):
    a = ''
    for film in library.get_favourite_list():
        a += str(film)
        a += '\n'
    bot.send_message(message.from_user.id, a)


@bot.message_handler(commands=['add_fav'])
def add_favourite_film(message):
    bot.send_message(message.from_user.id, 'Введите название фильма')
    bot.register_next_step_handler(message, get_favourite_name)


def get_favourite_name(message):
    global film_name
    film_name = message.text
    library.set_favourite(film_name)


bot.polling()
