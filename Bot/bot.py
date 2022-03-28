import telebot
import urllib.request

token = '1456579231:AAEuVKN9ldiX_V64JqNhcg8ecpgllrcjnX0'
bot = telebot.TeleBot('1456579231:AAEuVKN9ldiX_V64JqNhcg8ecpgllrcjnX0')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('АД', 'ДМ', 'Матем', 'ПАСЗИ', 'ССПД', 'Физика', 'Философия', 'ЭТИвЗИ')

def check(message,k):
    if k != 'ад' and k != 'дм' and k != 'матем' and k != 'пасзи' and k != 'сспд' and k != 'физика' and k != 'философия' and k != 'этивзи':
        bot.send_message(message.chat.id, 'Что-то на татарском')
        return 1
    return 0

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Приветики. Дз по какому предмету ты хочешь узнать', reply_markup=keyboard2)

@bot.message_handler(commands=['add'])
def add_message(message):
    bot.send_message(message.chat.id, 'Какой предмет ты хочешь добавить?', reply_markup=keyboard2)

@bot.message_handler(content_types=['text'])
def second_text(message):
    k = message.text.lower()
    if check(message, k) == 0 :
        bot.send_message(message.chat.id, '')

@bot.message_handler(content_types=["document"])
def handle_docs_file(message):
    document_id = message.document.file_id
    file_info = bot.get_file(document_id)
    urllib.request.urlretrieve(f'http://api.telegram.org/file/bot{token}/{file_info.file_path}', file_info.file_path)

bot.polling()