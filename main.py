import telebot
from telebot import types

bot = telebot.TeleBot('5513608925:AAGZtxWBqbCy1XJ5NdKBuIzlOsNdDoDdsnA')

@bot.message_handler(commands=['help', 'start', 'restart'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item2 = types.KeyboardButton('Розклад уроків 📝')
    item3 = types.KeyboardButton('Розклад дзвінків 🛎️')
    item33 = types.KeyboardButton('Книжки 📚')
    item6 = types.KeyboardButton('/start')
    markup.add(item2, item3, item6, item33 )
    bot.send_message(message.chat.id,
                     'Привіт, {0.first_name}!'.format(message.from_user), reply_markup = markup)

    @bot.message_handler(content_types=['text'])
    def bot_message(message):
        if message.chat.type == 'private':
            if message.text == 'Розклад дзвінків 🛎️':
                bot.send_message(message.chat.id, ' \nРозклад дзвінків на понеділок:  \n1) 8.45   \n2) 9:10 - 9:55   \n3) 10:00 - 10:45  \n4) 11:00 - 11:45   \n5) 12:00 - 12:45   \n6) 13:00 - 13:45   \n7) 14:00 - 14:45   \n8) 15:00 - 15:45     \nРозклад дзвінків вівторок-п`ятниця:  \n1) 8:50 - 9:35   \n2) 10:00 - 10:45   \n3) 11:00 - 11:45  \n4) 12:00 - 12:45   \n5) 13:00 - 13:45   \n6) 14:00 - 14:45   \n7) 15:00 - 15:45   \n8) 16:00 - 16:45')
            elif message.text == 'Розклад уроків 📝':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item3 = types.KeyboardButton('Понеділок')
                item4 = types.KeyboardButton('Вівторок')
                item5 = types.KeyboardButton('Середа')
                item6 = types.KeyboardButton('Четвер')
                item7 = types.KeyboardButton('Пятниця')
                back = types.KeyboardButton('⬅️Назад')
                start2 = types.KeyboardButton('/restart')
                markup.add(item3, item4, item5, item6, item7, back, start2)
                bot.send_message(message.chat.id, 'Розклад уроків 📝', reply_markup = markup )
            elif message.text == 'Понеділок':
                bot.send_message(message.chat.id,
                                 '\n1.Година спілкування'
                                 '\n2.Хімія'
                                 '\n3.Історія України/географія'
                                 '\n4.Мистецтво'
                                 '\n5.Хімія/захист України'
                                 '\n6.Українська мова'
                                 '\n7.Математика'
                                 '\n8.Математика')
            elif message.text == 'Вівторок':
                bot.send_message(message.chat.id,
                                 '\n1.Математика'
                                 '\n2.Англійська мова'
                                 '\n3.Українська література'
                                 '\n4.Фізична культура'
                                 '\n5.Математика'
                                 '\n6.Фізика'
                                 '\n7.Історія України'
                                 '\n8. - ')

            elif message.text == 'Середа':
                bot.send_message(message.chat.id,
                                 '\n1.Англійська мова'
                                 '\n2.Фізична культура'
                                 '\n3.Всесвітня історія'
                                 '\n4.Фізика'
                                 '\n5.Математика'
                                 '\n6.Біологія'
                                 '\n7.Математика'
                                 '\n8. - ')
            elif message.text == 'Четвер':
                bot.send_message(message.chat.id,
                                 '\n1.Громадянська освіта'
                                 '\n2.Фізична культура'
                                 '\n3.Українська література'
                                 '\n4.Зарубіжна література'
                                 '\n5.Математика'
                                 '\n6.Захист України'
                                 '\n7.Математика'
                                 '\n8. -  ')
            elif message.text == 'Пятниця':
                bot.send_message(message.chat.id,
                                 '\n1.Математика'
                                 '\n2.Українська мова'
                                 '\n3.Інформатика'
                                 '\n4.Біологія'
                                 '\n5.Громадянська освіта'
                                 '\n6.Фізика'
                                 '\n7.Географія'
                                 '\n8.Фінансова грамотність')
            elif message.text == '⬅️Назад':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item2 = types.KeyboardButton('Розклад уроків 📝')
                item3 = types.KeyboardButton('Розклад дзвінків 🛎️')
                item33 = types.KeyboardButton('Книжки 📚')
                item6 = types.KeyboardButton('/start')
                markup.add(item2, item3, item6, item33 )
                bot.send_message(message.chat.id, '⬅️Назад' , reply_markup = markup)

            if message.text == 'Книжки 📚':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item8 = types.KeyboardButton('1')
                    item9 = types.KeyboardButton('2')
                    item10 = types.KeyboardButton('3')
                    item11 = types.KeyboardButton('4')
                    item12 = types.KeyboardButton('5')
                    item13 = types.KeyboardButton('6')
                    item14 = types.KeyboardButton('7')
                    item15 = types.KeyboardButton('8')
                    item16 = types.KeyboardButton('9')
                    item17 = types.KeyboardButton('10')
                    item18 = types.KeyboardButton('11')
                    item19 = types.KeyboardButton('12')
                    item20 = types.KeyboardButton('13')
                    item21 = types.KeyboardButton('14')
                    item22 = types.KeyboardButton('15')
                    item23 = types.KeyboardButton('16')
                    item24 = types.KeyboardButton('17')
                    back2 = types.KeyboardButton('⬅️  Назад')
                    start2 = types.KeyboardButton('/restart')
                    markup.add(item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, back2, start2)
                    bot.send_message(message.chat.id, '\n1.Алгебра'
                                                      '\n2.Англійська мова'
                                                      '\n3.Біологія і Екологія'
                                                      '\n4Всесвітня історія'
                                                      '\n5.Географія'
                                                      '\n6.Геометрія'
                                                      '\n7.Громадянська освіта'
                                                      '\n8.Зарубіжна література'
                                                      '\n9.Захист України'
                                                      '\n10.Інформатика'
                                                      '\n11.Історія України'
                                                      '\n12.Мистецтво'
                                                      '\n13.Українська література'
                                                      '\n14.Українська мова'
                                                      '\n15.Фізика'
                                                      '\n16.Фінансова грамотність'
                                                      '\n17.Хімія'
                                                      ,
                                     reply_markup=markup)
            elif message.text == '⬅️  Назад':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item2 = types.KeyboardButton('Розклад уроків 📝')
                    item3 = types.KeyboardButton('Розклад дзвінків 🛎️')
                    item33 = types.KeyboardButton('Книжки 📚')
                    item6 = types.KeyboardButton('/start')
                    markup.add(item2, item3, item6, item33 )
                    bot.send_message(message.chat.id, '⬅️  Назад', reply_markup=markup)
            elif message.text == '1':
                with open("Алгебра.pdf", "rb") as file:
                    f = file.read()
                    bot.send_document(message.chat.id, open(r'Алгебра.pdf' , 'rb' ))
         #   elif message.text == '2':
          #     with open("", "rb") as file:
           #        f = file.read()
            #       bot.send_document(message.chat.id, open(r'Алгебра.pdf' , 'rb' ))
            elif message.text == '3':
                with open("Біологія і Екологія.pdf", "rb") as file:
                    f = file.read()
                    bot.send_document(message.chat.id, open(r'Біологія і Екологія.pdf', 'rb'))
            elif message.text == '4':
                with open("Всесвітня Історія.pdf", "rb") as file:
                    f = file.read()
                    bot.send_document(message.chat.id, open(r'Всесвітня Історія.pdf', 'rb'))
            elif message.text == '5':
                with open("Географія.pdf", "rb") as file:
                    f = file.read()
                    bot.send_document(message.chat.id, open(r'Географія.pdf', 'rb'))
           # elif message.text == '6':
            #    with open("", "rb") as file:
             #       f = file.read()
              #      bot.send_document(message.chat.id, open(r'', 'rb'))
            elif message.text == '7':
                with open("Громадянська освіта.pdf", "rb") as file:
                    f = file.read()
                    bot.send_document(message.chat.id, open(r'Громадянська освіта.pdf', 'rb'))
           # elif message.text == '8':
            #    with open("", "rb") as file:
             #       f = file.read()
              #      bot.send_document(message.chat.id, open(r'', 'rb'))
            elif message.text == '9':
                with open("Захист Вітчизни.pdf", "rb") as file:
                    f = file.read()
                    bot.send_document(message.chat.id, open(r'Захист Вітчизни.pdf', 'rb'))
            elif message.text == '10':
                with open("Інформатика.pdf", "rb") as file:
                    f = file.read()
                    bot.send_document(message.chat.id, open(r'Інформатика.pdf', 'rb'))
            elif message.text == '11':
                with open("Історія України.pdf", "rb") as file:
                    f = file.read()
                    bot.send_document(message.chat.id, open(r'Історія України.pdf', 'rb'))
          #  elif message.text == '12':
             #   with open("", "rb") as file:
                #    f = file.read()
                  #  bot.send_document(message.chat.id, open(r'', 'rb'))
            elif message.text == '13':
                with open("Українська література.pdf", "rb") as file:
                    f = file.read()
                    bot.send_document(message.chat.id, open(r'Українська література.pdf', 'rb'))
            elif message.text == '14':
                with open("Українська мова.pdf", "rb") as file:
                    f = file.read()
                    bot.send_document(message.chat.id, open(r'Українська мова.pdf', 'rb'))
            elif message.text == '15':
                with open("Фізика.pdf", "rb") as file:
                    f = file.read()
                    bot.send_document(message.chat.id, open(r'Фізика.pdf', 'rb'))
            elif message.text == '16':
                with open("Фінансова грамотність.pdf", "rb") as file:
                    f = file.read()
                    bot.send_document(message.chat.id, open(r'Фінансова грамотність.pdf', 'rb'))
            elif message.text == '17':
                with open("Хімія.pdf", "rb") as file:
                    f = file.read()
                    bot.send_document(message.chat.id, open(r'Хімія.pdf', 'rb'))


bot.polling(none_stop = True)
