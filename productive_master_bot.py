#  MODULES  #

import telebot
import sqlite3
import datetime
import time

#  CONFIG  #

import config

#  DATABASE  #

import database

#  MARKUPS  #

import inline_markups
import reply_markups

#  TASKS  #

import create_task
import complete_task
import delete_task
import edit_inline

#  DISPLAY  #

import display_statistics

#  FINANCE  #

import create_card
import finance

import notes





#  LIBRARY VARIABLES  #

bot = telebot.TeleBot(config.token)

db = sqlite3.connect("productive_master_bot.db", check_same_thread=False)
sql = db.cursor()

current_date = datetime.datetime.now().date()

current_month = datetime.datetime.now().strftime('%B')





#  USER TABLES  #

sql.execute("CREATE TABLE IF NOT EXISTS user_access (id INTEGER, username TEXT, firstname TEXT, lastname TEXT, date TIMESTAMP)")
db.commit()

sql.execute("CREATE TABLE IF NOT EXISTS user_finance (id INTEGER, status TEXT, currency TEXT, balance INTEGER)")
db.commit()

sql.execute("CREATE TABLE IF NOT EXISTS user_profile (id INTEGER, date TIMESTAMP, active INTEGER)")
db.commit()



#  DAY TABLES  #

sql.execute("CREATE TABLE IF NOT EXISTS monday (id INTEGER, task_1 TEXT, task_2 TEXT, task_3 TEXT, task_4 TEXT, task_5 TEXT, task_6 TEXT, task_7 TEXT, task_8 TEXT, task_9 TEXT, task_10 TEXT)")
db.commit()

sql.execute("CREATE TABLE IF NOT EXISTS tuesday (id INTEGER, task_1 TEXT, task_2 TEXT, task_3 TEXT, task_4 TEXT, task_5 TEXT, task_6 TEXT, task_7 TEXT, task_8 TEXT, task_9 TEXT, task_10 TEXT)")
db.commit()

sql.execute("CREATE TABLE IF NOT EXISTS wednesday (id INTEGER, task_1 TEXT, task_2 TEXT, task_3 TEXT, task_4 TEXT, task_5 TEXT, task_6 TEXT, task_7 TEXT, task_8 TEXT, task_9 TEXT, task_10 TEXT)")
db.commit()

sql.execute("CREATE TABLE IF NOT EXISTS thursday (id INTEGER, task_1 TEXT, task_2 TEXT, task_3 TEXT, task_4 TEXT, task_5 TEXT, task_6 TEXT, task_7 TEXT, task_8 TEXT, task_9 TEXT, task_10 TEXT)")
db.commit()

sql.execute("CREATE TABLE IF NOT EXISTS friday (id INTEGER, task_1 TEXT, task_2 TEXT, task_3 TEXT, task_4 TEXT, task_5 TEXT, task_6 TEXT, task_7 TEXT, task_8 TEXT, task_9 TEXT, task_10 TEXT)")
db.commit()

sql.execute("CREATE TABLE IF NOT EXISTS saturday (id INTEGER, task_1 TEXT, task_2 TEXT, task_3 TEXT, task_4 TEXT, task_5 TEXT, task_6 TEXT, task_7 TEXT, task_8 TEXT, task_9 TEXT, task_10 TEXT)")
db.commit()

sql.execute("CREATE TABLE IF NOT EXISTS sunday (id INTEGER, task_1 TEXT, task_2 TEXT, task_3 TEXT, task_4 TEXT, task_5 TEXT, task_6 TEXT, task_7 TEXT, task_8 TEXT, task_9 TEXT, task_10 TEXT)")
db.commit()



#  MONTH TABLES  #

sql.execute("CREATE TABLE IF NOT EXISTS finance_statistics (id INTEGER, January INTEGER, February INTEGER, March INTEGER, April INTEGER, May INTEGER, June INTEGER, July INTEGER, August INTEGER, September INTEGER, October INTEGER, November INTEGER, December INTEGER)")
db.commit()

sql.execute("CREATE TABLE IF NOT EXISTS income_statistics (id INTEGER, January INTEGER, February INTEGER, March INTEGER, April INTEGER, May INTEGER, June INTEGER, July INTEGER, August INTEGER, September INTEGER, October INTEGER, November INTEGER, December INTEGER)")
db.commit()

sql.execute("CREATE TABLE IF NOT EXISTS outcome_statistics (id INTEGER, January INTEGER, February INTEGER, March INTEGER, April INTEGER, May INTEGER, June INTEGER, July INTEGER, August INTEGER, September INTEGER, October INTEGER, November INTEGER, December INTEGER)")
db.commit()

sql.execute("CREATE TABLE IF NOT EXISTS tasks_statistics (id INTEGER, January INTEGER, February INTEGER, March INTEGER, April INTEGER, May INTEGER, June INTEGER, July INTEGER, August INTEGER, September INTEGER, October INTEGER, November INTEGER, December INTEGER)")
db.commit()





@bot.message_handler(commands=['forward'])
def Forward(message):

    if message.chat.id == 284929331:

        sql.execute("SELECT id FROM user_finance WHERE status == 'No'")
        users = sql.fetchall()

        for row in users:

            try:

                bot.send_message(row[0],    "<b>"
                                            "Вы еще не открыли свой виртуальный финансовый баланс ?  🤔"
                                            "\n\nПора открыть виртуальную карту и начать следить за статистиками ваших доходов и расходов  🙄💸"
                                            "</b>", parse_mode="html", reply_markup=inline_markups.create_balance_inline)
            except:

                pass

        else:

            bot.send_message(message.chat.id, "Рассылка закончена !")







#  START  #

@bot.message_handler(commands=['start'])
def start(message):

    sql.execute(f'''SELECT id FROM user_access WHERE id = {message.chat.id}''')
    user_id = sql.fetchone()

    if user_id is None:

        database.add_start(message)

        bot.send_message(message.chat.id,   '<b>'
                                            'Добро пожаловать в  "Productive Master Bot"  😊'
                                            '\n\nНаш бот поможет вам управлять своими ежедневными задачами, финансами и временем  ⏱ 💸'
                                            '</b>', parse_mode='html', reply_markup=reply_markups.menu_button)

        time.sleep(2)

        bot.send_message(message.chat.id,   "<b>Если нужна помощь, воспользуйтесь командой  -  /help</b>", parse_mode='html')

        bot.send_message('@He7Vd1e2fE',
                          f"New User ⚠" + "\n\n" +
                          f"User ID:  " + str(message.chat.id) +
                          f"\nUsername:  @" + str(message.from_user.username) +
                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                          f"\nLast Name:  " + str(message.from_user.last_name))


        with open(f'Notes/{message.chat.id}.txt', 'a+') as file:
            file.write(f"- - - - - Ваши Заметки - - - - -\n\n\n")
            file.close()



    else:

        bot.send_message(message.chat.id, "<b> 🏠  Главное меню: </b>", parse_mode='html', reply_markup=reply_markups.menu_button)



#  HELP  #

@bot.message_handler(commands=['help'])
def help(message):

    bot.send_message(message.chat.id,   '\n<b>📝  Задачи</b>  -  где вы можете <b>создавать</b>, <b>изменять</b>, <b>выполнять</b> и <b>удалять</b> свои задачи.'
                                        '\n\n<b>💸  Финанс</b>  -  где вы можете создать свой безопасный <b>финансовый счёт</b> и следить за статистикой своих <b>доходов</b> и <b>расходов</b>.'
                                        '\n\n<b>📁  История</b>  -  где вы найдете <b>дату</b> и <b>время</b> своих <b>доходов</b> и <b>расходов</b>.'
                                        '\n\n<b>📔  Заметки</b>  -  куда вы можете записывать свои <b>маловажные задачи</b> или <b>упоминания</b>.'
                                        '\n\n<b>📊  Статистика</b>  -  где вы можете найти <b>статистику</b> ваших <b>выполненных задач</b>, <b>доходов</b>, <b>расходов</b> и <b>финансового состояния</b> за текущий месяц. А также присутствует <b>фильтр</b> статистики:  "<b>По месяцам</b>" и "<b>За всё время</b>".'
                                        '\n\n<b>👤  Профиль</b>  -  где находятся ваши данные как: "<b>ID</b>", "<b>Дата Регистрации</b>", "<b>Статус</b>" и "<b>Активность</b>"',
                                        parse_mode='html', reply_markup=inline_markups.hide_inline)



#  BALANCE  #

@bot.message_handler(commands=['balance'])
def balance(message):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT balance FROM user_finance WHERE ID = {message.chat.id}''')
    user_balance = sql.fetchone()[0]

    bot.send_message(message.chat.id, f"<b> Ваш баланс составляет:</b>   <i>{user_balance}  {user_currency}</i>", parse_mode="html", reply_markup=inline_markups.hide_inline)




#  INCOME  #

@bot.message_handler(commands=['income'])
def income(message):

        sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {message.chat.id}''')
        user_currency = sql.fetchone()[0]

        add_balance = bot.send_message(message.chat.id, f"<b> Введите сумму дохода в {user_currency}: </b>", parse_mode="html")
        bot.register_next_step_handler(add_balance, finance.add_balance)



#  WASTE  #

@bot.message_handler(commands=['waste'])
def waste(message):

        sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {message.chat.id}''')
        user_currency = sql.fetchone()[0]

        waste_balance = bot.send_message(message.chat.id, f"<b> Введите сумму расхода в {user_currency}: </b>", parse_mode="html")
        bot.register_next_step_handler(waste_balance, finance.waste_balance)










#  TEXT  #

@bot.message_handler(content_types=["text"])
def text(message):


    #  ACTIONS  #

    bot.send_message('@HwiYf2rOVC42',   f"User ID:  " + str(message.chat.id) +
                                        f"\nUsername:  @" + str(message.from_user.username) +
                                        f"\nFirst Name:  " + str(message.from_user.first_name) +
                                        f"\nLast Name:  " + str(message.from_user.last_name) +
                                        f"\nAction:  " + str(message.text))




    #  DB DATA  #

    #  PROFILE  #

    sql.execute(f'''SELECT date FROM user_profile WHERE ID = {message.chat.id}''')
    user_date = sql.fetchone()[0]

    sql.execute(f'''SELECT active FROM user_profile WHERE ID = {message.chat.id}''')
    user_active = sql.fetchone()[0]

    #  FINANCE  #

    sql.execute(f'''SELECT status FROM user_finance WHERE ID = {message.chat.id}''')
    user_finance_status = sql.fetchone()[0]

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {message.chat.id}''')
    user_currency = sql.fetchone()[0]

    #  STATISTICS  #

    sql.execute(f'''SELECT {current_month} FROM tasks_statistics WHERE ID = {message.chat.id}''')
    current_tasks = sql.fetchone()[0]

    sql.execute(f'''SELECT {current_month} FROM income_statistics WHERE ID = {message.chat.id}''')
    current_income = sql.fetchone()[0]

    sql.execute(f'''SELECT {current_month} FROM outcome_statistics WHERE ID = {message.chat.id}''')
    current_outcome = sql.fetchone()[0]

    sql.execute(f'''SELECT {current_month} FROM finance_statistics WHERE ID = {message.chat.id}''')
    current_condition = sql.fetchone()[0]





    #  STATISTICS  #

    if message.text == "📊  Статистика":

        if user_currency == "[валюта не указана]":

            bot.send_message(message.chat.id, f"<b>Ваша статистика за этот месяц:</b>"
                                              f"\n\n<b>📝  Выполненные задачи:</b>  {current_tasks}"
                                              f"\n\n<b>📥  Доходы:</b>  {current_income}  {user_currency}"
                                              f"\n<b>📤  Расходы:</b>  {current_outcome}  {user_currency}"
                                              f"\n\n<b>📊  Финансовое состояние:</b>  <i>{current_condition}</i>  {user_currency}",
                                              parse_mode="html", reply_markup=inline_markups.statistics_inline)

        else:

            if current_condition > 0:

                bot.send_message(message.chat.id,   f"<b>Ваша статистика за этот месяц:</b>"
                                                    f"\n\n<b>📝  Выполненные задачи:</b>   <i>{current_tasks}</i>"
                                                    f"\n\n<b>📥  Доходы:</b>   <i>{current_income}  {user_currency}</i>"
                                                    f"\n<b>📤  Расходы:</b>   <i>{current_outcome}  {user_currency}</i>"
                                                    f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{current_condition}  {user_currency}</i>",
                                                    parse_mode="html", reply_markup=inline_markups.statistics_inline)

            elif current_condition < 0:

                bot.send_message(message.chat.id,   f"<b>Ваша статистика за этот месяц:</b>"
                                                    f"\n\n<b>📝  Выполненные задачи:</b>   <i>{current_tasks}</i>"
                                                    f"\n\n<b>📥  Доходы:</b>   <i>{current_income}  {user_currency}</i>"
                                                    f"\n<b>📤  Расходы:</b>   <i>{current_outcome}  {user_currency}</i>"
                                                    f"\n\n<b>📉  Финансовое состояние:</b>   <i>{current_condition}  {user_currency}</i>",
                                                    parse_mode="html", reply_markup=inline_markups.statistics_inline)

            else:

                bot.send_message(message.chat.id,   f"<b>Ваша статистика за этот месяц:</b>"
                                                    f"\n\n<b>📝  Выполненные задачи:</b>   <i>{current_tasks}</i>"
                                                    f"\n\n<b>📥  Доходы:</b>   <i>{current_income}  {user_currency}</i>"
                                                    f"\n<b>📤  Расходы:</b>   <i>{current_outcome}  {user_currency}</i>"
                                                    f"\n\n<b>📊  Финансовое состояние:</b>   <i>{current_condition}  {user_currency}</i>",
                                                    parse_mode="html", reply_markup=inline_markups.statistics_inline)



    #  TASKS  #

    if message.text == "📝  Задачи":
        bot.send_message(message.chat.id, "<b> Выберите день недели: </b>", parse_mode="html", reply_markup=inline_markups.day_inline)



    #  NOTES  #

    if message.text == "📔  Заметки":

        with open(f'Notes/{message.chat.id}.txt', 'rb') as file:
            bot.send_document(message.chat.id, file, caption="<b> Выберите действие вашей заметки: </b>", parse_mode="html", reply_markup=inline_markups.notes_inline)








    #  FINANCE  #

    if message.text == "💸  Финанс":

        if user_finance_status == "Yes":

            bot.send_message(message.chat.id, "<b> Выберите финансовый раздел: </b>", parse_mode="html", reply_markup=inline_markups.finance_inline)

        if user_finance_status == "No":

            bot.send_message(message.chat.id, "<b>"
                                              "У вас еще нет виртуальной карты ❗️\n\nНажмите на кнопку ниже чтобы создать виртуальную карту  👇"
                                              "</b>", parse_mode="html", reply_markup=inline_markups.create_balance_inline)



    #  HISTORY  #

    if message.text == "📁  История":

        bot.send_message(message.chat.id, "<b> Выберите раздел истории ваших процессов: </b>", parse_mode="html", reply_markup=inline_markups.history_inline)



    #  PROFILE  #

    if message.text == "👤  Профиль":

        if user_active < 100:

            bot.send_message(message.chat.id,   f"<b>🗓  Дата регистрации:</b>  {user_date}"
                                                f"\n<b>🆔  ID:</b>  {message.chat.id}"
                                                f"\n\n<b>🔰  Статус:</b>  Новичок"
                                                f"\n<b>⚡️  Активность:</b>  {user_active} / 100",
                                                parse_mode="html", reply_markup=inline_markups.profile_inline)

        elif user_active >= 100 and user_active < 350:

            bot.send_message(message.chat.id,   f"<b>🗓  Дата регистрации:</b>  {user_date}"
                                                f"\n<b>🆔  ID:</b>  {message.chat.id}"
                                                f"\n\n<b>🔰  Статус:</b>  Опытный"
                                                f"\n<b>⚡️  Активность:</b>  {user_active} / 350",
                                                parse_mode="html", reply_markup=inline_markups.profile_inline)

        elif user_active >= 350 and user_active < 850:

            bot.send_message(message.chat.id,   f"<b>🗓  Дата регистрации:</b>  {user_date}"
                                                f"\n<b>🆔  ID:</b>  {message.chat.id}"
                                                f"\n\n<b>🔰  Статус:</b>  Продвинутый"
                                                f"\n<b>⚡️  Активность:</b>  {user_active} / 850",
                                                parse_mode="html", reply_markup=inline_markups.profile_inline)

        elif user_active >= 850 and user_active < 1500:

            bot.send_message(message.chat.id,   f"<b>🗓  Дата регистрации:</b>  {user_date}"
                                                f"\n<b>🆔  ID:</b>  {message.chat.id}"
                                                f"\n\n<b>🔰  Статус:</b>  Профессионал"
                                                f"\n<b>⚡️  Активность:</b>  {user_active} / 1500",
                                                parse_mode="html", reply_markup=inline_markups.profile_inline)

        elif user_active > 1500:

            bot.send_message(message.chat.id,   f"<b>🗓  Дата регистрации:</b>  {user_date}"
                                                f"\n<b>🆔  ID:</b>  {message.chat.id}"
                                                f"\n\n<b>🔰  Статус:</b>  Мастер  👑"
                                                f"\n<b>⚡️  Активность:</b>  {user_active}",
                                                parse_mode="html", reply_markup=inline_markups.profile_inline)
















#  CALLBACKS  #

@bot.callback_query_handler(func = lambda call: True)
def callbacks(call):



    #  CREATE CARD  #

    if call.data == "create_card":

        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "<b> Выберите валюту вашего баланса: </b>", parse_mode="html", reply_markup=inline_markups.currency_inline)


    #  SELECT CURRENCY  #

    if call.data == "USD":

        sql.execute(f'''UPDATE user_finance SET (currency) = ('USD') WHERE ID = "{call.message.chat.id}"''')
        db.commit()

        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

        create_balance = bot.send_message(call.message.chat.id, "<b> Укажите баланс вашей карты: </b>", parse_mode="html")
        bot.register_next_step_handler(create_balance, create_card.create_balance)


    if call.data == "RUB":

        sql.execute(f'''UPDATE user_finance SET (currency) = ('RUB') WHERE ID = "{call.message.chat.id}"''')
        db.commit()

        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

        create_balance = bot.send_message(call.message.chat.id, "<b> Укажите баланс вашей карты: </b>", parse_mode="html")
        bot.register_next_step_handler(create_balance, create_card.create_balance)


    if call.data == "UZS":

        sql.execute(f'''UPDATE user_finance SET (currency) = ('UZS') WHERE ID = "{call.message.chat.id}"''')
        db.commit()

        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

        create_balance = bot.send_message(call.message.chat.id, "<b> Укажите баланс вашей карты: </b>", parse_mode="html")
        bot.register_next_step_handler(create_balance, create_card.create_balance)










    #  BALANCE  #

    if call.data == "balance":

        sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
        user_currency = sql.fetchone()[0]

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b> Ваш баланс составляет:</b>   ******  <i>{user_currency}</i>", parse_mode="html", reply_markup=inline_markups.balance_inline_1)


    #  EDIT BALANCE  #

    if call.data == "edit_balance":

        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

        new_balance = bot.send_message(call.message.chat.id, "<b> Укажите ваш новый баланс: </b>", parse_mode="html")
        bot.register_next_step_handler(new_balance, finance.edit_balance)



    #  SHOW BALANCE  #

    if call.data == "show_balance":

        sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
        user_currency = sql.fetchone()[0]

        sql.execute(f'''SELECT balance FROM user_finance WHERE ID = {call.message.chat.id}''')
        user_balance = sql.fetchone()[0]

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b> Ваш баланс составляет:</b>   <i>{user_balance}  {user_currency}</i>", parse_mode="html", reply_markup=inline_markups.balance_inline_2)


    #  HIDE BALANCE  #

    if call.data == "hide_balance":

        sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
        user_currency = sql.fetchone()[0]

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b> Ваш баланс составляет:</b>   ******  <i>{user_currency}</i>", parse_mode="html", reply_markup=inline_markups.balance_inline_1)





    #  (ADD & WASTE) FINANCE #

    if call.data == "add_finance":

        sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
        user_currency = sql.fetchone()[0]

        add_balance = bot.send_message(call.message.chat.id, f"<b> Введите сумму дохода в {user_currency}: </b>", parse_mode="html")
        bot.register_next_step_handler(add_balance, finance.add_balance)


    if call.data == "waste_finance":

        sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
        user_currency = sql.fetchone()[0]

        waste_balance = bot.send_message(call.message.chat.id, f"<b> Введите сумму расхода в {user_currency}: </b>", parse_mode="html")
        bot.register_next_step_handler(waste_balance, finance.waste_balance)





    #  INCOME & OUTCOME  #

    if call.data == "income":

        sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
        user_currency = sql.fetchone()[0]

        sql.execute(f'''SELECT {current_month} FROM income_statistics WHERE ID = {call.message.chat.id}''')
        current_income = sql.fetchone()[0]

        bot.send_message(call.message.chat.id, f"<b> Ваши доходы за этот месяц:</b>   <i>{current_income}  {user_currency}</i>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b> Ваши доходы за этот месяц:</b>  {current_income} {user_currency}", parse_mode="html", reply_markup=inline_markups.back_finance_inline)


    if call.data == "outcome":

        sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
        user_currency = sql.fetchone()[0]

        sql.execute(f'''SELECT {current_month} FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
        current_outcome = sql.fetchone()[0]

        bot.send_message(call.message.chat.id, f"<b> Ваши расходы за этот месяц:</b>   <i>{current_outcome}  {user_currency}</i>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b> Ваши расходы за этот месяц:</b>  {current_outcome} {user_currency}", parse_mode="html", reply_markup=inline_markups.back_finance_inline)










    #  HISTORY  #

    if call.data == "income_history":

        try:

            with open(f'History/Income/{call.message.chat.id}.txt', 'rb') as user_file:
                bot.send_document(call.message.chat.id, user_file, caption="<b> История ваших доходов: </b>", parse_mode="html")

        except:

            bot.send_message(call.message.chat.id, "<b> У вас еще не было доходов ❗️ </b>", parse_mode="html")



    if call.data == "outcome_history":

        try:

            with open(f'History/Outcome/{call.message.chat.id}.txt', 'rb') as user_file:
                bot.send_document(call.message.chat.id, user_file, caption="<b> История ваших расходов: </b>", parse_mode="html")

        except:

            bot.send_message(call.message.chat.id, "<b> У вас еще не было расходов ❗️ </b>", parse_mode="html")










    #  STATISTICS MONTH  #

    if call.data == "month_statistics":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b> Выберите месяц: </b>", parse_mode="html", reply_markup=inline_markups.month_statistics_inline)



    if call.data == "all_time_statistics":
        display_statistics.display_all_statistics(call)


    if call.data == "statistics_january":
        display_statistics.display_january_statistics(call)

    if call.data == "statistics_february":
        display_statistics.display_february_statistics(call)

    if call.data == "statistics_march":
        display_statistics.display_march_statistics(call)

    if call.data == "statistics_april":
        display_statistics.display_april_statistics(call)

    if call.data == "statistics_may":
        display_statistics.display_may_statistics(call)

    if call.data == "statistics_june":
        display_statistics.display_june_statistics(call)

    if call.data == "statistics_july":
        display_statistics.display_july_statistics(call)

    if call.data == "statistics_august":
        display_statistics.display_august_statistics(call)

    if call.data == "statistics_september":
        display_statistics.display_september_statistics(call)

    if call.data == "statistics_october":
        display_statistics.display_october_statistics(call)

    if call.data == "statistics_november":
        display_statistics.display_november_statistics(call)

    if call.data == "statistics_december":
        display_statistics.display_december_statistics(call)







    #  NOTES  #

    if call.data == "write_notes":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        user_notes = bot.send_message(call.message.chat.id, "<b> Напишите текст которого хотите написать: </b>", parse_mode="html")
        bot.register_next_step_handler(user_notes, notes.write_to_note)


    if call.data == "clear_notes":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        notes.clear_notes(call.message)










    #  TASK DAYS  #

    if call.data == "monday":
        edit_inline.edit_monday_inline_1(call)

    if call.data == "next_monday_tasks":
        edit_inline.edit_monday_inline_2(call)

    if call.data == "previous_monday_tasks":
        edit_inline.edit_monday_inline_1(call)


    if call.data == "tuesday":
        edit_inline.edit_tuesday_inline_1(call)

    if call.data == "next_tuesday_tasks":
        edit_inline.edit_tuesday_inline_2(call)

    if call.data == "previous_tuesday_tasks":
        edit_inline.edit_tuesday_inline_1(call)


    if call.data == "wednesday":
        edit_inline.edit_wednesday_inline_1(call)

    if call.data == "next_wednesday_tasks":
        edit_inline.edit_wednesday_inline_2(call)

    if call.data == "previous_wednesday_tasks":
        edit_inline.edit_wednesday_inline_1(call)


    if call.data == "thursday":
        edit_inline.edit_thursday_inline_1(call)

    if call.data == "next_thursday_tasks":
        edit_inline.edit_thursday_inline_2(call)

    if call.data == "previous_thursday_tasks":
        edit_inline.edit_thursday_inline_1(call)


    if call.data == "friday":
        edit_inline.edit_friday_inline_1(call)

    if call.data == "next_friday_tasks":
        edit_inline.edit_friday_inline_2(call)

    if call.data == "previous_friday_tasks":
        edit_inline.edit_friday_inline_1(call)


    if call.data == "saturday":
        edit_inline.edit_saturday_inline_1(call)

    if call.data == "next_saturday_tasks":
        edit_inline.edit_saturday_inline_2(call)

    if call.data == "previous_saturday_tasks":
        edit_inline.edit_saturday_inline_1(call)


    if call.data == "sunday":
        edit_inline.edit_sunday_inline_1(call)

    if call.data == "next_sunday_tasks":
        edit_inline.edit_sunday_inline_2(call)

    if call.data == "previous_sunday_tasks":
        edit_inline.edit_sunday_inline_1(call)










    #  CREATE TASKS  #

    #  MONDAY  #

    if call.data == "add_monday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        monday_task_1 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(monday_task_1, create_task.create_monday_task_1)

    if call.data == "add_monday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        monday_task_2 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(monday_task_2, create_task.create_monday_task_2)

    if call.data == "add_monday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        monday_task_3 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(monday_task_3, create_task.create_monday_task_3)

    if call.data == "add_monday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        monday_task_4 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(monday_task_4, create_task.create_monday_task_4)

    if call.data == "add_monday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        monday_task_5 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(monday_task_5, create_task.create_monday_task_5)

    if call.data == "add_monday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        monday_task_6 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(monday_task_6, create_task.create_monday_task_6)

    if call.data == "add_monday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        monday_task_7 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(monday_task_7, create_task.create_monday_task_7)

    if call.data == "add_monday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        monday_task_8 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(monday_task_8, create_task.create_monday_task_8)

    if call.data == "add_monday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        monday_task_9 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(monday_task_9, create_task.create_monday_task_9)

    if call.data == "add_monday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        monday_task_10 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(monday_task_10, create_task.create_monday_task_10)

    #  TUESDAY  #

    if call.data == "add_tuesday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        tuesday_task_1 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(tuesday_task_1, create_task.create_tuesday_task_1)

    if call.data == "add_tuesday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        tuesday_task_2 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(tuesday_task_2, create_task.create_tuesday_task_2)

    if call.data == "add_tuesday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        tuesday_task_3 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(tuesday_task_3, create_task.create_tuesday_task_3)

    if call.data == "add_tuesday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        tuesday_task_4 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(tuesday_task_4, create_task.create_tuesday_task_4)

    if call.data == "add_tuesday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        tuesday_task_5 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(tuesday_task_5, create_task.create_tuesday_task_5)

    if call.data == "add_tuesday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        tuesday_task_6 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(tuesday_task_6, create_task.create_tuesday_task_6)

    if call.data == "add_tuesday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        tuesday_task_7 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(tuesday_task_7, create_task.create_tuesday_task_7)

    if call.data == "add_tuesday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        tuesday_task_8 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(tuesday_task_8, create_task.create_tuesday_task_8)

    if call.data == "add_tuesday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        tuesday_task_9 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(tuesday_task_9, create_task.create_tuesday_task_9)

    if call.data == "add_tuesday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        tuesday_task_10 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(tuesday_task_10, create_task.create_tuesday_task_10)

    #  WEDNESDAY  #

    if call.data == "add_wednesday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        wednesday_task_1 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(wednesday_task_1, create_task.create_wednesday_task_1)

    if call.data == "add_wednesday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        wednesday_task_2 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(wednesday_task_2, create_task.create_wednesday_task_2)

    if call.data == "add_wednesday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        wednesday_task_3 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(wednesday_task_3, create_task.create_wednesday_task_3)

    if call.data == "add_wednesday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        wednesday_task_4 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(wednesday_task_4, create_task.create_wednesday_task_4)

    if call.data == "add_wednesday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        wednesday_task_5 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(wednesday_task_5, create_task.create_wednesday_task_5)

    if call.data == "add_wednesday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        wednesday_task_6 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(wednesday_task_6, create_task.create_wednesday_task_6)

    if call.data == "add_wednesday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        wednesday_task_7 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(wednesday_task_7, create_task.create_wednesday_task_7)

    if call.data == "add_wednesday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        wednesday_task_8 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(wednesday_task_8, create_task.create_wednesday_task_8)

    if call.data == "add_wednesday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        wednesday_task_9 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(wednesday_task_9, create_task.create_wednesday_task_9)

    if call.data == "add_wednesday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        wednesday_task_10 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(wednesday_task_10, create_task.create_wednesday_task_10)

    #  THURSDAY  #

    if call.data == "add_thursday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        thursday_task_1 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(thursday_task_1, create_task.create_thursday_task_1)

    if call.data == "add_thursday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        thursday_task_2 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(thursday_task_2, create_task.create_thursday_task_2)

    if call.data == "add_thursday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        thursday_task_3 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(thursday_task_3, create_task.create_thursday_task_3)

    if call.data == "add_thursday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        thursday_task_4 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(thursday_task_4, create_task.create_thursday_task_4)

    if call.data == "add_thursday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        thursday_task_5 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(thursday_task_5, create_task.create_thursday_task_5)

    if call.data == "add_thursday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        thursday_task_6 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(thursday_task_6, create_task.create_thursday_task_6)

    if call.data == "add_thursday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        thursday_task_7 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(thursday_task_7, create_task.create_thursday_task_7)

    if call.data == "add_thursday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        thursday_task_8 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(thursday_task_8, create_task.create_thursday_task_8)

    if call.data == "add_thursday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        thursday_task_9 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(thursday_task_9, create_task.create_thursday_task_9)

    if call.data == "add_thursday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        thursday_task_10 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(thursday_task_10, create_task.create_thursday_task_10)

    #  FRIDAY  #

    if call.data == "add_friday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        friday_task_1 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(friday_task_1, create_task.create_friday_task_1)

    if call.data == "add_friday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        friday_task_2 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(friday_task_2, create_task.create_friday_task_2)

    if call.data == "add_friday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        friday_task_3 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(friday_task_3, create_task.create_friday_task_3)

    if call.data == "add_friday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        friday_task_4 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(friday_task_4, create_task.create_friday_task_4)

    if call.data == "add_friday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        friday_task_5 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(friday_task_5, create_task.create_friday_task_5)

    if call.data == "add_friday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        friday_task_6 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(friday_task_6, create_task.create_friday_task_6)

    if call.data == "add_friday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        friday_task_7 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(friday_task_7, create_task.create_friday_task_7)

    if call.data == "add_friday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        friday_task_8 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(friday_task_8, create_task.create_friday_task_8)

    if call.data == "add_friday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        friday_task_9 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(friday_task_9, create_task.create_friday_task_9)

    if call.data == "add_friday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        friday_task_10 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(friday_task_10, create_task.create_friday_task_10)

    #  SATURDAY  #

    if call.data == "add_saturday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        saturday_task_1 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(saturday_task_1, create_task.create_saturday_task_1)

    if call.data == "add_saturday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        saturday_task_2 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(saturday_task_2, create_task.create_saturday_task_2)

    if call.data == "add_saturday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        saturday_task_3 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(saturday_task_3, create_task.create_saturday_task_3)

    if call.data == "add_saturday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        saturday_task_4 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(saturday_task_4, create_task.create_saturday_task_4)

    if call.data == "add_saturday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        saturday_task_5 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(saturday_task_5, create_task.create_saturday_task_5)

    if call.data == "add_saturday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        saturday_task_6 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(saturday_task_6, create_task.create_saturday_task_6)

    if call.data == "add_saturday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        saturday_task_7 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(saturday_task_7, create_task.create_saturday_task_7)

    if call.data == "add_saturday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        saturday_task_8 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(saturday_task_8, create_task.create_saturday_task_8)

    if call.data == "add_saturday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        saturday_task_9 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(saturday_task_9, create_task.create_saturday_task_9)

    if call.data == "add_saturday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        saturday_task_10 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(saturday_task_10, create_task.create_saturday_task_10)

    #  SUNDAY  #

    if call.data == "add_sunday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        sunday_task_1 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(sunday_task_1, create_task.create_sunday_task_1)

    if call.data == "add_sunday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        sunday_task_2 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(sunday_task_2, create_task.create_sunday_task_2)

    if call.data == "add_sunday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        sunday_task_3 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(sunday_task_3, create_task.create_sunday_task_3)

    if call.data == "add_sunday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        sunday_task_4 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(sunday_task_4, create_task.create_sunday_task_4)

    if call.data == "add_sunday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        sunday_task_5 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(sunday_task_5, create_task.create_sunday_task_5)

    if call.data == "add_sunday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        sunday_task_6 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(sunday_task_6, create_task.create_sunday_task_6)

    if call.data == "add_sunday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        sunday_task_7 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(sunday_task_7, create_task.create_sunday_task_7)

    if call.data == "add_sunday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        sunday_task_8 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(sunday_task_8, create_task.create_sunday_task_8)

    if call.data == "add_sunday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        sunday_task_9 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(sunday_task_9, create_task.create_sunday_task_9)

    if call.data == "add_sunday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        sunday_task_10 = bot.send_message(call.message.chat.id, "<b> Напишите задачу: </b>", parse_mode="html")
        bot.register_next_step_handler(sunday_task_10, create_task.create_sunday_task_10)










    #  COMPLETE TASKS  #

    #  MONDAY  #

    if call.data == "complete_monday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_monday_task_1(call.message)

    if call.data == "complete_monday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_monday_task_2(call.message)

    if call.data == "complete_monday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_monday_task_3(call.message)

    if call.data == "complete_monday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_monday_task_4(call.message)

    if call.data == "complete_monday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_monday_task_5(call.message)

    if call.data == "complete_monday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_monday_task_6(call.message)

    if call.data == "complete_monday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_monday_task_7(call.message)

    if call.data == "complete_monday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_monday_task_8(call.message)

    if call.data == "complete_monday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_monday_task_9(call.message)

    if call.data == "complete_monday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_monday_task_10(call.message)

    #  TUESDAY  #

    if call.data == "complete_tuesday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_tuesday_task_1(call.message)

    if call.data == "complete_tuesday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_tuesday_task_2(call.message)

    if call.data == "complete_tuesday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_tuesday_task_3(call.message)

    if call.data == "complete_tuesday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_tuesday_task_4(call.message)

    if call.data == "complete_tuesday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_tuesday_task_5(call.message)

    if call.data == "complete_tuesday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_tuesday_task_6(call.message)

    if call.data == "complete_tuesday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_tuesday_task_7(call.message)

    if call.data == "complete_tuesday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_tuesday_task_8(call.message)

    if call.data == "complete_tuesday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_tuesday_task_9(call.message)

    if call.data == "complete_tuesday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_tuesday_task_10(call.message)

    #  WEDNESDAY  #

    if call.data == "complete_wednesday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_wednesday_task_1(call.message)

    if call.data == "complete_wednesday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_wednesday_task_2(call.message)

    if call.data == "complete_wednesday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_wednesday_task_3(call.message)

    if call.data == "complete_wednesday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_wednesday_task_4(call.message)

    if call.data == "complete_wednesday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_wednesday_task_5(call.message)

    if call.data == "complete_wednesday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_wednesday_task_6(call.message)

    if call.data == "complete_wednesday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_wednesday_task_7(call.message)

    if call.data == "complete_wednesday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_wednesday_task_8(call.message)

    if call.data == "complete_wednesday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_wednesday_task_9(call.message)

    if call.data == "complete_wednesday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_wednesday_task_10(call.message)

    #  THURSDAY  #

    if call.data == "complete_thursday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_thursday_task_1(call.message)

    if call.data == "complete_thursday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_thursday_task_2(call.message)

    if call.data == "complete_thursday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_thursday_task_3(call.message)

    if call.data == "complete_thursday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_thursday_task_4(call.message)

    if call.data == "complete_thursday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_thursday_task_5(call.message)

    if call.data == "complete_thursday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_thursday_task_6(call.message)

    if call.data == "complete_thursday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_thursday_task_7(call.message)

    if call.data == "complete_thursday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_thursday_task_8(call.message)

    if call.data == "complete_thursday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_thursday_task_9(call.message)

    if call.data == "complete_thursday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_thursday_task_10(call.message)

    #  FRIDAY  #

    if call.data == "complete_friday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_friday_task_1(call.message)

    if call.data == "complete_friday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_friday_task_2(call.message)

    if call.data == "complete_friday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_friday_task_3(call.message)

    if call.data == "complete_friday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_friday_task_4(call.message)

    if call.data == "complete_friday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_friday_task_5(call.message)

    if call.data == "complete_friday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_friday_task_6(call.message)

    if call.data == "complete_friday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_friday_task_7(call.message)

    if call.data == "complete_friday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_friday_task_8(call.message)

    if call.data == "complete_friday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_friday_task_9(call.message)

    if call.data == "complete_friday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_friday_task_10(call.message)

    #  SATURDAY  #

    if call.data == "complete_saturday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_saturday_task_1(call.message)

    if call.data == "complete_saturday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_saturday_task_2(call.message)

    if call.data == "complete_saturday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_saturday_task_3(call.message)

    if call.data == "complete_saturday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_saturday_task_4(call.message)

    if call.data == "complete_saturday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_saturday_task_5(call.message)

    if call.data == "complete_saturday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_saturday_task_6(call.message)

    if call.data == "complete_saturday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_saturday_task_7(call.message)

    if call.data == "complete_saturday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_saturday_task_8(call.message)

    if call.data == "complete_saturday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_saturday_task_9(call.message)

    if call.data == "complete_saturday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_saturday_task_10(call.message)

    #  SUNDAY  #

    if call.data == "complete_sunday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_sunday_task_1(call.message)

    if call.data == "complete_sunday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_sunday_task_2(call.message)

    if call.data == "complete_sunday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_sunday_task_3(call.message)

    if call.data == "complete_sunday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_sunday_task_4(call.message)

    if call.data == "complete_sunday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_sunday_task_5(call.message)

    if call.data == "complete_sunday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_sunday_task_6(call.message)

    if call.data == "complete_sunday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_sunday_task_7(call.message)

    if call.data == "complete_sunday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_sunday_task_8(call.message)

    if call.data == "complete_sunday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_sunday_task_9(call.message)

    if call.data == "complete_sunday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        complete_task.complete_sunday_task_10(call.message)







    #  DELETE TASKS  #

    #  MONDAY  #

    if call.data == "delete_monday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_monday_task_1(call.message)

    if call.data == "delete_monday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_monday_task_2(call.message)

    if call.data == "delete_monday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_monday_task_3(call.message)

    if call.data == "delete_monday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_monday_task_4(call.message)

    if call.data == "delete_monday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_monday_task_5(call.message)

    if call.data == "delete_monday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_monday_task_6(call.message)

    if call.data == "delete_monday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_monday_task_7(call.message)

    if call.data == "delete_monday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_monday_task_8(call.message)

    if call.data == "delete_monday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_monday_task_9(call.message)

    if call.data == "delete_monday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_monday_task_10(call.message)

    #  TUESDAY  #

    if call.data == "delete_tuesday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_tuesday_task_1(call.message)

    if call.data == "delete_tuesday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_tuesday_task_2(call.message)

    if call.data == "delete_tuesday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_tuesday_task_3(call.message)

    if call.data == "delete_tuesday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_tuesday_task_4(call.message)

    if call.data == "delete_tuesday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_tuesday_task_5(call.message)

    if call.data == "delete_tuesday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_tuesday_task_6(call.message)

    if call.data == "delete_tuesday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_tuesday_task_7(call.message)

    if call.data == "delete_tuesday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_tuesday_task_8(call.message)

    if call.data == "delete_tuesday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_tuesday_task_9(call.message)

    if call.data == "delete_tuesday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_tuesday_task_10(call.message)

    #  WEDNESDAY  #

    if call.data == "delete_wednesday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_wednesday_task_1(call.message)

    if call.data == "delete_wednesday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_wednesday_task_2(call.message)

    if call.data == "delete_wednesday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_wednesday_task_3(call.message)

    if call.data == "delete_wednesday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_wednesday_task_4(call.message)

    if call.data == "delete_wednesday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_wednesday_task_5(call.message)

    if call.data == "delete_wednesday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_wednesday_task_6(call.message)

    if call.data == "delete_wednesday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_wednesday_task_7(call.message)

    if call.data == "delete_wednesday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_wednesday_task_8(call.message)

    if call.data == "delete_wednesday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_wednesday_task_9(call.message)

    if call.data == "delete_wednesday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_wednesday_task_10(call.message)

    #  THURSDAY  #

    if call.data == "delete_thursday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_thursday_task_1(call.message)

    if call.data == "delete_thursday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_thursday_task_2(call.message)

    if call.data == "delete_thursday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_thursday_task_3(call.message)

    if call.data == "delete_thursday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_thursday_task_4(call.message)

    if call.data == "delete_thursday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_thursday_task_5(call.message)

    if call.data == "delete_thursday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_thursday_task_6(call.message)

    if call.data == "delete_thursday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_thursday_task_7(call.message)

    if call.data == "delete_thursday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_thursday_task_8(call.message)

    if call.data == "delete_thursday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_thursday_task_9(call.message)

    if call.data == "delete_thursday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_thursday_task_10(call.message)

    #  FRIDAY  #

    if call.data == "delete_friday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_friday_task_1(call.message)

    if call.data == "delete_friday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_friday_task_2(call.message)

    if call.data == "delete_friday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_friday_task_3(call.message)

    if call.data == "delete_friday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_friday_task_4(call.message)

    if call.data == "delete_friday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_friday_task_5(call.message)

    if call.data == "delete_friday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_friday_task_6(call.message)

    if call.data == "delete_friday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_friday_task_7(call.message)

    if call.data == "delete_friday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_friday_task_8(call.message)

    if call.data == "delete_friday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_friday_task_9(call.message)

    if call.data == "delete_friday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_friday_task_10(call.message)

    #  SATURDAY  #

    if call.data == "delete_saturday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_saturday_task_1(call.message)

    if call.data == "delete_saturday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_saturday_task_2(call.message)

    if call.data == "delete_saturday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_saturday_task_3(call.message)

    if call.data == "delete_saturday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_saturday_task_4(call.message)

    if call.data == "delete_saturday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_saturday_task_5(call.message)

    if call.data == "delete_saturday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_saturday_task_6(call.message)

    if call.data == "delete_saturday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_saturday_task_7(call.message)

    if call.data == "delete_saturday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_saturday_task_8(call.message)

    if call.data == "delete_saturday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_saturday_task_9(call.message)

    if call.data == "delete_saturday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_saturday_task_10(call.message)

    #  SUNDAY  #

    if call.data == "delete_sunday_task_1":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_sunday_task_1(call.message)

    if call.data == "delete_sunday_task_2":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_sunday_task_2(call.message)

    if call.data == "delete_sunday_task_3":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_sunday_task_3(call.message)

    if call.data == "delete_sunday_task_4":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_sunday_task_4(call.message)

    if call.data == "delete_sunday_task_5":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_sunday_task_5(call.message)

    if call.data == "delete_sunday_task_6":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_sunday_task_6(call.message)

    if call.data == "delete_sunday_task_7":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_sunday_task_7(call.message)

    if call.data == "delete_sunday_task_8":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_sunday_task_8(call.message)

    if call.data == "delete_sunday_task_9":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_sunday_task_9(call.message)

    if call.data == "delete_sunday_task_10":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        delete_task.delete_sunday_task_10(call.message)







    if call.data == "status":
        bot.send_message(call.message.chat.id,  "<b>"
                                                "🔰  Статус  -  это звание пользователя за набранные активности."
                                                "\n\n🔰  Новичок  -  0 / 100  ⚡️"
                                                "\n🔰  Опытный  -  100 / 350  ⚡️"
                                                "\n🔰  Продвинутый  -  350 / 850  ⚡️"
                                                "\n🔰  Профессионал  -  850 / 1500  ⚡️"
                                                "\n🔰  Мастер  -  1500  👑"
                                                "</b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


    if call.data == "active":
        bot.send_message(call.message.chat.id,  "<b>"
                                                "⚡️  Активность  -  это очки пользователя за выполненные задачи."
                                                "\n\nЗа каждые выполненные задачи пользователь получает  -  5  ⚡️"
                                                "\n\nНабирая активность пользователи могут достигнуть нового статуса  🔰"
                                                "</b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



    #  DELETE MESSAGE  #

    if call.data == "hide_message":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    if call.data == "cancel":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "<b> Отменено </b>", parse_mode="html")




    #  BACK  #

    if call.data == "back_week":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b> Выберите день недели: </b>", parse_mode="html", reply_markup=inline_markups.day_inline)

    if call.data == "back_statistics":
        display_statistics.display_current_statistics(call)

    if call.data == "back_finance":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b> Выберите финансовый раздел: </b>", parse_mode="html", reply_markup=inline_markups.finance_inline)




#  LAUNCH THE BOT  #

if __name__=='__main__':

    while True:

        try:

            bot.polling(non_stop=True, interval=0)

        except Exception as e:

            bot.send_message(284929331, "<b> 🆘  ERROR  🆘 </b>", parse_mode="html")
            print(e)
            time.sleep(5)
            continue