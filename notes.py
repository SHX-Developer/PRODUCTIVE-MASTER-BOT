#  MODULES  #

import telebot
import sqlite3


import  config

import inline_markups


#  LIBRARY VARIABLES  #

bot = telebot.TeleBot(config.token)

db = sqlite3.connect("productive_master_bot.db", check_same_thread=False)
sql = db.cursor()



def write_to_note(message):

    with open(f'Notes/{message.chat.id}.txt', 'a+') as file:
        file.write(f"{message.text}\n")
        file.close()

        with open(f'Notes/{message.chat.id}.txt', 'rb') as file:
            bot.send_document(message.chat.id, file, caption="<b> Ваши заметки добавлены  ✅ </b>", parse_mode="html", reply_markup=inline_markups.notes_inline)



def clear_notes(message):

    with open(f'Notes/{message.chat.id}.txt', 'w') as file:
        file.write('')
        file.write(f'- - - - - Ваши Заметки - - - - -\n\n\n')
        file.close()

        bot.send_message(message.chat.id, "<b> Ваши заметки очищены  ✅ </b>", parse_mode="html")

        with open(f'Notes/{message.chat.id}.txt', 'rb') as file:
            bot.send_document(message.chat.id, file, caption="<b> Выберите действие вашей заметки: </b>", parse_mode="html", reply_markup=inline_markups.notes_inline)