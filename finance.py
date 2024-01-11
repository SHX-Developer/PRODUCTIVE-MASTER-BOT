import telebot
import sqlite3
import datetime

import inline_markups
import config


bot = telebot.TeleBot(config.token)

db = sqlite3.connect("productive_master_bot.db", check_same_thread=False)
sql = db.cursor()

current_month = datetime.datetime.now().strftime('%B')
current_date = datetime.date.today()

now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")


def edit_balance(message):


    #  EDIT  #

    sql.execute(f'''UPDATE user_finance SET (balance) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    bot.send_message(message.chat.id, "<b> Ваш баланс изменён  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



    #  DISPLAY  #

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT balance FROM user_finance WHERE ID = {message.chat.id}''')
    user_balance = sql.fetchone()[0]

    bot.send_message(message.chat.id, f"<b> Ваш баланс составляет:</b>   <i>{user_balance}  {user_currency}</i>", parse_mode="html", reply_markup=inline_markups.balance_inline_2)






#  ADD FINANCE  #

def add_balance(message):
    
    if message.text == "0":

        sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {message.chat.id}''')
        user_currency = sql.fetchone()[0]
        
        bot.send_message(message.chat.id, f"<b> Сумма должна быть больше:   0 {user_currency} ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
    
    else:

        try:

            int(message.text)

            sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {message.chat.id}''')
            user_currency = sql.fetchone()[0]

            sql.execute(f'''UPDATE user_finance SET balance = balance + {message.text} WHERE ID = "{message.chat.id}"''')
            db.commit()

            sql.execute(f'''UPDATE income_statistics SET {current_month} = {current_month} + {message.text} WHERE ID = "{message.chat.id}"''')
            db.commit()

            sql.execute(f'''UPDATE finance_statistics SET {current_month} = {current_month} + {message.text} WHERE ID = "{message.chat.id}"''')
            db.commit()

            bot.send_message(message.chat.id, f"<b> На ваш баланс добавлены:</b>   <i>{message.text}  {user_currency}</i>  ✅", parse_mode="html", reply_markup=inline_markups.hide_inline)

            with open(f'History/Income/{message.chat.id}.txt', 'a+') as file:
                file.write(f"[{current_date}] [{current_time}]:   +{message.text} {user_currency}\n")
                file.close()

        except:

            bot.send_message(message.chat.id, f"<b> Сумма должна включать только числа ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



        




#  WASTE FINANCE  #

def waste_balance(message):

    if message.text == "0":

        sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {message.chat.id}''')
        user_currency = sql.fetchone()[0]
        
        bot.send_message(message.chat.id, f"<b> Сумма должна быть больше:   0 {user_currency} ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
    
    else:

        try:

            int(message.text)
        
            sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {message.chat.id}''')
            user_currency = sql.fetchone()[0]

            sql.execute(f'''UPDATE user_finance SET balance = balance - {message.text} WHERE ID = "{message.chat.id}"''')
            db.commit()

            sql.execute(f'''UPDATE outcome_statistics SET {current_month} = {current_month} - {message.text} WHERE ID = "{message.chat.id}"''')
            db.commit()

            sql.execute(f'''UPDATE finance_statistics SET {current_month} = {current_month} - {message.text} WHERE ID = "{message.chat.id}"''')
            db.commit()

            bot.send_message(message.chat.id, f"<b> Из вашего баланса отняты:</b>   <i>{message.text}  {user_currency}</i>  ✅", parse_mode="html", reply_markup=inline_markups.hide_inline)

            with open(f'History/Outcome/{message.chat.id}.txt', 'a+') as file:
                file.write(f"[{current_date}] [{current_time}]:   -{message.text} {user_currency}\n")
                file.close()
        
        except:

            bot.send_message(message.chat.id, f"<b> Сумма должна включать только числа ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)





