import telebot
from telebot import apihelper
from telebot import types

#todo сделать ограничение по колличеству баллов в день, чтобы избежать накрутки
#todo прдумать структуру для базы, но в другом модуле, прописать скрипт
#todo сделать процедуру регистрации пользователей


# apihelper.proxy = {''}
apihelper.proxy = {''}
bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Получить задание')
    itembtn2 = types.KeyboardButton('Проверить задание')
    itembtn3 = types.KeyboardButton('Узнать баллы')
    itembtn4 = types.KeyboardButton('Справка/сообщить об ошибке')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id,
                     'Привет, ты написал мне /start, теперь выбери пункт меню и  '
                     'дальньейшем можешь пользоваться только кнопками меню',
                     reply_markup=markup)




@bot.message_handler(content_types=['text'])
def first_menu(message):
    if message.text == 'Получить задание':
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Подтвердить выполнение')
        itembtn2 = types.KeyboardButton('На главную')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id,
                             'Привет, твое задание на сегодня: "///вставка задание из базы данных///"',
                             reply_markup=markup)
    elif message.text == 'На главную':
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Получить задание')
        itembtn2 = types.KeyboardButton('Проверить задание')
        itembtn3 = types.KeyboardButton('Узнать баллы')
        itembtn4 = types.KeyboardButton('Справка/сообщить об ошибке')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
        bot.send_message(message.chat.id,
                         'Можешь выбрать интересующий пункт меню',
                         reply_markup=markup)

    elif message.text == 'Проверить задание':
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Первое задание')
        itembtn2 = types.KeyboardButton('Второе задание')
        itembtn3 = types.KeyboardButton('Третье задание')
        itembtn4 = types.KeyboardButton('На главную')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
        bot.send_message(message.chat.id,
                         'Выберите задание для проверки',
                         reply_markup=markup)
    elif message.text == 'Узнать баллы':
        bot.send_message(message.chat.id,
                         'У вас "Подсчитать колличество баллов, вставить из базы данных"')
    elif message.text == 'Справка/сообщить об ошибке':
        bot.send_message(message.chat.id,
                     'Вы можете задать вопрос или сообщить об ошибке в директ инстаграм по этой ссылке: https://www.instagram.com/beautybox.ru/')
# @bot.message_handler(commands=['taketask'])
# def start_message(message):
#     bot.send_message(message.chat.id,
#                      'Привет, вот твое задание, как выполнишь, обязательно отправь его на проверку',
#                      reply_markup=itembtn1)


bot.polling(timeout=5000)
