from telebot import TeleBot
from film import FilmLibrary

bot = TeleBot('1015483974:AAFiuGMQB1CewhRP4JFbamvUZBjP9z3ytmw')
library = FilmLibrary()


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.from_user.id, 'Привет')


@bot.message_handler(commands='add')
def add(message):
    bot.send_message(message.from_user.id, 'Введите название фильма')


bot.polling()