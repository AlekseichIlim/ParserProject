import telebot
from telebot import types

from config import TELEGRAM_TOKEN
from main import engine, session

from src.db_manager import get_themes_list, get_rating_list
from src.functions import get_compilation_problems, main


bot = telebot.TeleBot(TELEGRAM_TOKEN)

markup = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton(text="Обновить базу данных")
btn2 = types.KeyboardButton(text="Получить подборку задач")
markup.row(btn1, btn2)


@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(message.chat.id,
                     f"Привет, {message.from_user.first_name}! Это бот получения подборки из 10 задач, по заданной сложности и тематике, с сервиса Codeforces",
                     reply_markup=markup
                     )

    bot.send_message(message.chat.id, "Выберите действие:")
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == "Обновить базу данных":
        main(engine, session)
        bot.send_message(message.chat.id, "База обновлена")
        bot.register_next_step_handler(message, on_click)
    elif message.text == "Получить подборку задач":
        after_text_1(message)


@bot.message_handler(content_types=['text'])
def after_text_1(message):

    bot.send_message(message.from_user.id, "Введите тему из предложенных вариантов:")
    bot.send_message(message.from_user.id, f'Темы:{get_themes_list(session)}')
    bot.register_next_step_handler(message, after_text_2)


@bot.message_handler(content_types=['text'])
def after_text_2(message):

    bot.send_message(message.from_user.id,
                     "Введите сложность из предложенных вариантов:")
    bot.send_message(message.chat.id, f'Сложность:{get_rating_list(session)}')
    theme = message.text.lower()
    bot.register_next_step_handler(message, compilation, theme)


@bot.message_handler()
def compilation(message, theme):

    if message.text.isdigit() is False:
        bot.send_message(message.chat.id, "Проверьте введенные данные")
        after_text_1(message)

    else:
        rating = int(message.text)
        bot.send_message(message.chat.id, "Получение подборки...")
        problems = get_compilation_problems(session, theme, rating)
        count = len(problems)
        num = 0
        if count != 0:
            if count < 10:
                bot.send_message(message.chat.id, f"Всего найдено задач по данному запросу: {count}")
            for i in problems:
                markup_2 = types.InlineKeyboardMarkup()
                markup_2.add(types.InlineKeyboardButton('Перейти к задаче:',
                                                        url=f'https://codeforces.com/problemset/problem/{i.contest_id}/{i.index}'))
                num += 1
                bot.send_message(message.chat.id, f'{num}# {str(i)}', reply_markup=markup_2)
            bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, f"По вашему запросу ничего не найдено.")
            after_text_1(message)
        bot.register_next_step_handler(message, on_click)


bot.polling(none_stop=True)
