import telebot

bot = telebot.TeleBot('1456579231:AAEuVKN9ldiX_V64JqNhcg8ecpgllrcjnX0')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    flag = message
    if message.text.lower() == 'жак пидр':
        bot.send_message(message.chat.id, 'безусловно!')
    else:
        bot.send_message(message.chat.id, 'Свергнем Жака')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()