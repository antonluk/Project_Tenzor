# https://habr.com/ru/post/448310/
# https://mastergroosha.github.io/telegram-tutorial/docs/lesson_08/
# https://habr.com/ru/post/335886/

import telebot

bot = telebot.TeleBot('1025478928:AAECV6bQDwqY_Wsaf7f-itSYq0rbK5oHT_U')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    else:
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)


bot.polling()
