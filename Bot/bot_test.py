@bot.message_handler(content_types=['text'])
def second_text(message):
    k = message.text.lower()
    if k != 'ад' and k != 'дм' and k != 'матем' and k != 'пасзи' and k != 'сспд' and k != 'физика' and k != 'философия' and k != 'этивзи' and k != 'узнать' and k != 'добавить':
        bot.send_message(message.chat.id, 'Что-то на татарском')
    else:
        if k == 'узнать':
            flag1 = 1
            bot.send_message(message.chat.id, 'Выбери предмет',reply_markup=keyboard2)
        elif k == 'добавить':
            flag1 = 2
            bot.send_message(message.chat.id, 'Выбери предмет', reply_markup=keyboard2)
        else:
            if flag1 == 0:
                bot.send_message(message.chat.id, 'Приветики. Хочешь узнать ДЗ или добавить ДЗ?', reply_markup=keyboard1)
            elif flag1 == 1:
                bot.send_message(message.chat.id, 'Сейчас посмотрю...')
                if k != 'ад':
                    pass
                elif k != 'дм':
                    pass
                elif k != 'матем':
                    pass
                elif k != 'пасзи':
                    pass
                elif k != 'сспд':
                    pass
                elif k != 'физика':
                    pass
                elif k != 'философия':
                    pass
                elif k != 'этивзи':
                    pass