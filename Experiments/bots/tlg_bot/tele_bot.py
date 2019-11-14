import telebot

bot = telebot.TeleBot('720297361:AAELpP-TP_8VhnDgw5C0rN6rBzPd5p1M8eQ')


@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    except Exception as exc:
        print(f"Error {exc}")


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Hi my lord')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Bye my lord')


bot.polling(none_stop=True, interval=1)
