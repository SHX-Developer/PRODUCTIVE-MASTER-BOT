import telebot
import sqlite3
import datetime

import config

import inline_markups



bot = telebot.TeleBot(config.token)

db = sqlite3.connect("productive_master_bot.db", check_same_thread=False)
sql = db.cursor()

current_month = datetime.datetime.now().strftime('%B')



def display_all_statistics(call):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT January, February, March, April, May, June, July, August, September, October, November, December FROM tasks_statistics WHERE ID = {call.message.chat.id}''')
    tasks_data = sql.fetchall()

    sql.execute(f'''SELECT January, February, March, April, May, June, July, August, September, October, November, December FROM income_statistics WHERE ID = {call.message.chat.id}''')
    income_data = sql.fetchall()

    sql.execute(f'''SELECT January, February, March, April, May, June, July, August, September, October, November, December FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
    outcome_data = sql.fetchall()

    sql.execute(f'''SELECT January, February, March, April, May, June, July, August, September, October, November, December FROM finance_statistics WHERE ID = {call.message.chat.id}''')
    condition_data = sql.fetchall()

    for tasks_row in tasks_data:

        total_tasks = tasks_row[0] + tasks_row[1] + tasks_row[2] + tasks_row[3] + tasks_row[4] + tasks_row[5] + tasks_row[6] + tasks_row[7] + tasks_row[8] + tasks_row[9] + tasks_row[10] + tasks_row[11]

        for income_row in income_data:

            total_income = income_row[0] + income_row[1] + income_row[2] + income_row[3] + income_row[4] + income_row[5] + income_row[6] + income_row[7] + income_row[8] + income_row[9] + income_row[10] + income_row[11]

            for outcome_row in outcome_data:

                total_outcome = outcome_row[0] + outcome_row[1] + outcome_row[2] + outcome_row[3] + outcome_row[4] + outcome_row[5] + outcome_row[6] + outcome_row[7] + outcome_row[8] + outcome_row[9] + outcome_row[10] + outcome_row[11]

                for condition_row in condition_data:

                    total_condition = condition_row[0] + condition_row[1] + condition_row[2] + condition_row[3] + condition_row[4] + condition_row[5] + condition_row[6] + condition_row[7] + condition_row[8] + condition_row[9] + condition_row[10] + condition_row[11]

                    if total_condition > 0:

                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Ваша статистика за всё время:</b>"
                                                                                                                    f"\n\n<b>📝  Выполненные задачи:</b>   <i>{total_tasks}</i>"
                                                                                                                    f"\n\n<b>📥  Доходы:</b>   <i>{total_income}  {user_currency}</i>"
                                                                                                                    f"\n<b>📤  Расходы:</b>   <i>{total_outcome}  {user_currency}</i>"
                                                                                                                    f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{total_condition}  {user_currency}</i>",
                                                                                                                    parse_mode="html", reply_markup=inline_markups.month_statistics_inline)
                    elif total_condition < 0:

                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Ваша статистика за всё время:</b>"
                                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{total_tasks}</i>"
                                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{total_income}  {user_currency}</i>"
                                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{total_outcome}  {user_currency}</i>"
                                                                                                                     f"\n\n<b>📉  Финансовое состояние:</b>   <i>{total_condition}  {user_currency}</i>",
                                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

                    else:

                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Ваша статистика за всё время:</b>"
                                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{total_tasks}</i>"
                                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{total_income}  {user_currency}</i>"
                                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{total_outcome}  {user_currency}</i>"
                                                                                                                     f"\n\n<b>📊  Финансовое состояние:</b>   <i>{total_condition}  {user_currency}</i>",
                                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)








#  CURRENT MONTH  #

def display_current_statistics(call):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT {current_month} FROM tasks_statistics WHERE ID = {call.message.chat.id}''')
    current_tasks = sql.fetchone()[0]

    sql.execute(f'''SELECT {current_month} FROM income_statistics WHERE ID = {call.message.chat.id}''')
    current_income = sql.fetchone()[0]

    sql.execute(f'''SELECT {current_month} FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
    current_outcome = sql.fetchone()[0]

    sql.execute(f'''SELECT {current_month} FROM finance_statistics WHERE ID = {call.message.chat.id}''')
    current_condition = sql.fetchone()[0]



    if current_condition > 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text =  f"<b>Ваша статистика за этот месяц:</b>"
                                                                                                        f"\n\n<b>📝  Выполненные задачи:</b>   <i>{current_tasks}</i>"
                                                                                                        f"\n\n<b>📥  Доходы:</b>   <i>{current_income}  {user_currency}</i>"
                                                                                                        f"\n<b>📤  Расходы:</b>   <i>{current_outcome}  {user_currency}</i>"
                                                                                                        f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{current_condition}  {user_currency}</i>",
                                                                                                        parse_mode="html", reply_markup=inline_markups.statistics_inline)

    elif current_condition < 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text =  f"<b>Ваша статистика за этот месяц:</b>"
                                                                                                        f"\n\n<b>📝  Выполненные задачи:</b>   <i>{current_tasks}</i>"
                                                                                                        f"\n\n<b>📥  Доходы:</b>   <i>{current_income}  {user_currency}</i>"
                                                                                                        f"\n<b>📤  Расходы:</b>   <i>{current_outcome}  {user_currency}</i>"
                                                                                                        f"\n\n<b>📉  Финансовое состояние:</b>   <i>{current_condition}  {user_currency}</i>",
                                                                                                        parse_mode="html", reply_markup=inline_markups.statistics_inline)
    
    else:
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text =  f"<b>Ваша статистика за этот месяц:</b>"
                                                                                                        f"\n\n<b>📝  Выполненные задачи:</b>   <i>{current_tasks}</i>"
                                                                                                        f"\n\n<b>📥  Доходы:</b>   <i>{current_income}  {user_currency}</i>"
                                                                                                        f"\n<b>📤  Расходы:</b>   <i>{current_outcome}  {user_currency}</i>"
                                                                                                        f"\n\n<b>📊  Финансовое состояние:</b>   <i>{current_condition}  {user_currency}</i>",
                                                                                                        parse_mode="html", reply_markup=inline_markups.statistics_inline)





#  JANUARY  #

def display_january_statistics(call):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT January FROM tasks_statistics WHERE ID = {call.message.chat.id}''')
    tasks = sql.fetchone()[0]

    sql.execute(f'''SELECT January FROM income_statistics WHERE ID = {call.message.chat.id}''')
    income = sql.fetchone()[0]

    sql.execute(f'''SELECT January FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
    outcome = sql.fetchone()[0]

    sql.execute(f'''SELECT January FROM finance_statistics WHERE ID = {call.message.chat.id}''')
    condition = sql.fetchone()[0]

    if condition > 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text =  f"<b>Статистика за январь:</b>" 
                                                                                                        f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                        f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                        f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                        f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{condition}  {user_currency}</i>",
                                                                                                        parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    elif condition < 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за январь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📉  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    else:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за январь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📊  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)



#  FEBRUARY  #

def display_february_statistics(call):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT February FROM tasks_statistics WHERE ID = {call.message.chat.id}''')
    tasks = sql.fetchone()[0]

    sql.execute(f'''SELECT February FROM income_statistics WHERE ID = {call.message.chat.id}''')
    income = sql.fetchone()[0]

    sql.execute(f'''SELECT February FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
    outcome = sql.fetchone()[0]

    sql.execute(f'''SELECT February FROM finance_statistics WHERE ID = {call.message.chat.id}''')
    condition = sql.fetchone()[0]

    if condition > 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text =  f"<b>Статистика за февраль:</b>" 
                                                                                                        f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                        f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                        f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                        f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{condition}  {user_currency}</i>",
                                                                                                        parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    elif condition < 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за февраль:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📉  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    else:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за февраль:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📊  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)



#  MARCH  #

def display_march_statistics(call):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT March FROM tasks_statistics WHERE ID = {call.message.chat.id}''')
    tasks = sql.fetchone()[0]

    sql.execute(f'''SELECT March FROM income_statistics WHERE ID = {call.message.chat.id}''')
    income = sql.fetchone()[0]

    sql.execute(f'''SELECT March FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
    outcome = sql.fetchone()[0]
    
    sql.execute(f'''SELECT March FROM finance_statistics WHERE ID = {call.message.chat.id}''')
    condition = sql.fetchone()[0]

    if condition > 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за март:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    elif condition < 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за март:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📉  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    else:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за март:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📊  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)



#  APRIL  #

def display_april_statistics(call):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT April FROM tasks_statistics WHERE ID = {call.message.chat.id}''')
    tasks = sql.fetchone()[0]

    sql.execute(f'''SELECT April FROM income_statistics WHERE ID = {call.message.chat.id}''')
    income = sql.fetchone()[0]

    sql.execute(f'''SELECT April FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
    outcome = sql.fetchone()[0]

    sql.execute(f'''SELECT April FROM finance_statistics WHERE ID = {call.message.chat.id}''')
    condition = sql.fetchone()[0]

    if condition > 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за апрель:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    elif condition < 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за апрель:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📉  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    else:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за апрель:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📊  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)



#  MAY  #

def display_may_statistics(call):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT May FROM tasks_statistics WHERE ID = {call.message.chat.id}''')
    tasks = sql.fetchone()[0]

    sql.execute(f'''SELECT May FROM income_statistics WHERE ID = {call.message.chat.id}''')
    income = sql.fetchone()[0]

    sql.execute(f'''SELECT May FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
    outcome = sql.fetchone()[0]

    sql.execute(f'''SELECT May FROM finance_statistics WHERE ID = {call.message.chat.id}''')
    condition = sql.fetchone()[0]

    if condition > 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за май:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    elif condition < 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за май:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📉  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    else:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за май:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📊  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)



#  JUNE  #

def display_june_statistics(call):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT June FROM tasks_statistics WHERE ID = {call.message.chat.id}''')
    tasks = sql.fetchone()[0]

    sql.execute(f'''SELECT June FROM income_statistics WHERE ID = {call.message.chat.id}''')
    income = sql.fetchone()[0]

    sql.execute(f'''SELECT June FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
    outcome = sql.fetchone()[0]

    sql.execute(f'''SELECT June FROM finance_statistics WHERE ID = {call.message.chat.id}''')
    condition = sql.fetchone()[0]

    if condition > 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за июнь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    elif condition < 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за июнь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📉  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    else:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за июнь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📊  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)



#  JULY  #

def display_july_statistics(call):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT July FROM tasks_statistics WHERE ID = {call.message.chat.id}''')
    tasks = sql.fetchone()[0]

    sql.execute(f'''SELECT July FROM income_statistics WHERE ID = {call.message.chat.id}''')
    income = sql.fetchone()[0]

    sql.execute(f'''SELECT July FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
    outcome = sql.fetchone()[0]

    sql.execute(f'''SELECT July FROM finance_statistics WHERE ID = {call.message.chat.id}''')
    condition = sql.fetchone()[0]

    if condition > 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за июль:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    elif condition < 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за июль:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📉  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    else:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за июль:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📊  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)



#  AUGUST  #

def display_august_statistics(call):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT August FROM tasks_statistics WHERE ID = {call.message.chat.id}''')
    tasks = sql.fetchone()[0]

    sql.execute(f'''SELECT August FROM income_statistics WHERE ID = {call.message.chat.id}''')
    income = sql.fetchone()[0]

    sql.execute(f'''SELECT August FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
    outcome = sql.fetchone()[0]

    sql.execute(f'''SELECT August FROM finance_statistics WHERE ID = {call.message.chat.id}''')
    condition = sql.fetchone()[0]

    if condition > 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за август:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    elif condition < 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за август:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📉  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    else:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за август:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📊  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)



#  SEPTEMBER  #

def display_september_statistics(call):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT September FROM tasks_statistics WHERE ID = {call.message.chat.id}''')
    tasks = sql.fetchone()[0]

    sql.execute(f'''SELECT September FROM income_statistics WHERE ID = {call.message.chat.id}''')
    income = sql.fetchone()[0]

    sql.execute(f'''SELECT September FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
    outcome = sql.fetchone()[0]

    sql.execute(f'''SELECT September FROM finance_statistics WHERE ID = {call.message.chat.id}''')
    condition = sql.fetchone()[0]

    if condition > 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за сентябрь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    elif condition < 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за сентябрь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📉  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    else:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за сентябрь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📊  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)



#  OCTOBER  #

def display_october_statistics(call):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT October FROM tasks_statistics WHERE ID = {call.message.chat.id}''')
    tasks = sql.fetchone()[0]

    sql.execute(f'''SELECT October FROM income_statistics WHERE ID = {call.message.chat.id}''')
    income = sql.fetchone()[0]

    sql.execute(f'''SELECT October FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
    outcome = sql.fetchone()[0]

    sql.execute(f'''SELECT October FROM finance_statistics WHERE ID = {call.message.chat.id}''')
    condition = sql.fetchone()[0]

    if condition > 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за октябрь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    elif condition < 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за октябрь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📉  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    else:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за октябрь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📊  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)



#  NOVEMBER  #

def display_november_statistics(call):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT November FROM tasks_statistics WHERE ID = {call.message.chat.id}''')
    tasks = sql.fetchone()[0]

    sql.execute(f'''SELECT November FROM income_statistics WHERE ID = {call.message.chat.id}''')
    income = sql.fetchone()[0]

    sql.execute(f'''SELECT November FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
    outcome = sql.fetchone()[0]

    sql.execute(f'''SELECT November FROM finance_statistics WHERE ID = {call.message.chat.id}''')
    condition = sql.fetchone()[0]

    if condition > 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за ноябрь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    elif condition < 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за ноябрь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📉  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    else:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за ноябрь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📊  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)



#  DECEMBER  #

def display_december_statistics(call):

    sql.execute(f'''SELECT currency FROM user_finance WHERE ID = {call.message.chat.id}''')
    user_currency = sql.fetchone()[0]

    sql.execute(f'''SELECT December FROM tasks_statistics WHERE ID = {call.message.chat.id}''')
    tasks = sql.fetchone()[0]

    sql.execute(f'''SELECT December FROM income_statistics WHERE ID = {call.message.chat.id}''')
    income = sql.fetchone()[0]

    sql.execute(f'''SELECT December FROM outcome_statistics WHERE ID = {call.message.chat.id}''')
    outcome = sql.fetchone()[0]

    sql.execute(f'''SELECT December FROM finance_statistics WHERE ID = {call.message.chat.id}''')
    condition = sql.fetchone()[0]

    if condition > 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за декабрь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📈  Финансовое состояние:</b>   <i>+{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    elif condition < 0:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за декабрь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📉  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

    else:

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>Статистика за декабрь:</b>"
                                                                                                     f"\n\n<b>📝  Выполненные задачи:</b>   <i>{tasks}</i>"
                                                                                                     f"\n\n<b>📥  Доходы:</b>   <i>{income}  {user_currency}</i>"
                                                                                                     f"\n<b>📤  Расходы:</b>   <i>{outcome}  {user_currency}</i>"
                                                                                                     f"\n\n<b>📊  Финансовое состояние:</b>   <i>{condition}  {user_currency}</i>",
                                                                                                     parse_mode="html", reply_markup=inline_markups.month_statistics_inline)

