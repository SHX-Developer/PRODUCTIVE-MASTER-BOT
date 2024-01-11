import telebot
import sqlite3


import inline_markups
import config


bot = telebot.TeleBot(config.token)

db = sqlite3.connect("productive_master_bot.db", check_same_thread=False)
sql = db.cursor()







def create_balance(message):


    sql.execute(f'''UPDATE user_finance SET (balance) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    sql.execute(f'''UPDATE user_finance SET (status) = ('Yes') WHERE ID = "{message.chat.id}"''')
    db.commit()

    bot.send_message(message.chat.id, "<b> Ваша виртуальная карта создана  ✅ </b>", parse_mode="html", reply_markup=inline_markups.finance_inline)