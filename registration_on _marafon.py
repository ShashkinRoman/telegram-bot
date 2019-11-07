import os

import telebot
from telebot import apihelper
from telebot import types
from dotenv import load_dotenv
load_dotenv(verbose=True)
#todo сделать ограничение по колличеству баллов в день, чтобы избежать накрутки
#todo прдумать структуру для базы, но в другом модуле, прописать скрипт
#todo сделать процедуру регистрации пользователей


proxy = os.getenv('proxy')
sekret_token = os.getenv('secret_token')

# apihelper.proxy = {'http': 'http://59.127.168.43:3128', 'https': 'https://59.127.168.43:3128'}
apihelper.proxy = {'https': proxy}
bot = telebot.TeleBot(sekret_token)

@bot.message_handler(commands=['start'])
def first_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Зарегистрироваться на марафон')
    itembtn2 = types.KeyboardButton('Задать вопрс по марафону')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id,
                     'Добро пожаловать в бота beautyboox.ru, все доступные функции бота вы '
                     'можете увидеть ниже. Используйте кнопки, для навигации по боту'
                     ' и следуйте инструкциям',
                     reply_markup=markup)

#
@bot.message_handler(content_types=['text'])
def registration_step_one(message):
    bot.send_message(message.chat.id,
                    'Познакомимся? Введите и отправьте свое имя')
    # todo отправить имя в базу

@bot.message_handler(content_types=['text'])
def registration_step_two(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Изменить имя')
    markup.add(itembtn1)
    bot.send_message(message.chat.id,
                    'Приятно познакомиться "ВВЕДЕННОЕ ИМЯ", оставите свой телефончик? :)'
                    'Введите и отправьте телефон', reply_markup=markup)

    # todo отправить телефон в базу в базу

@bot.message_handler(content_types=['text'])
def registration_step_three(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Изменить телефон')
    markup.add(itembtn1)
    bot.send_message(message.chat.id,
                    'Отлично, теперь последний шаг,'
                    ' пришлите мне ссылку вашего рабочего Instagram аккаунта',
                     reply_markup=markup)

    # todo отправить телефон в базу в базу

@bot.message_handler(content_types=['text'])
def registration_step_three(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Изменить данные')
    itembtn2 = types.KeyboardButton('Подтвердить данные')
    markup.add(itembtn1)
    bot.send_message(message.chat.id,
                    'Отлично, теперь последний шаг,'
                    'проверьте свои данные "Номер телеофна, ник из инстаграм, имя'
                    'и подтвердите участие"',
                     reply_markup=markup)