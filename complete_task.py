import telebot
import sqlite3
import time
import datetime

import config
import display_task
import inline_markups



#  LIBRARY VARIABLES  #

bot = telebot.TeleBot(config.token)

db = sqlite3.connect("productive_master_bot.db", check_same_thread=False)
sql = db.cursor()

current_month = datetime.datetime.now().strftime('%B')





#  MONDAY  #

def complete_monday_task_1(message):

    sql.execute(f"SELECT task_1 FROM monday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE monday SET (task_1) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_1(message)

def complete_monday_task_2(message):

    sql.execute(f"SELECT task_2 FROM monday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE monday SET (task_2) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_1(message)

def complete_monday_task_3(message):

    sql.execute(f"SELECT task_3 FROM monday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE monday SET (task_3) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_1(message)

def complete_monday_task_4(message):

    sql.execute(f"SELECT task_4 FROM monday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE monday SET (task_4) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_1(message)

def complete_monday_task_5(message):

    sql.execute(f"SELECT task_5 FROM monday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE monday SET (task_5) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_1(message)

def complete_monday_task_6(message):

    sql.execute(f"SELECT task_6 FROM monday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE monday SET (task_6) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_2(message)

def complete_monday_task_7(message):

    sql.execute(f"SELECT task_7 FROM monday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE monday SET (task_7) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_2(message)

def complete_monday_task_8(message):

    sql.execute(f"SELECT task_8 FROM monday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE monday SET (task_8) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_2(message)

def complete_monday_task_9(message):

    sql.execute(f"SELECT task_9 FROM monday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE monday SET (task_9) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_2(message)

def complete_monday_task_10(message):

    sql.execute(f"SELECT task_10 FROM monday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE monday SET (task_10) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_monday_tasks_2(message)





#  TUESDAY  #

def complete_tuesday_task_1(message):

    sql.execute(f"SELECT task_1 FROM tuesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE tuesday SET (task_1) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_1(message)

def complete_tuesday_task_2(message):

    sql.execute(f"SELECT task_2 FROM tuesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE tuesday SET (task_2) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_1(message)

def complete_tuesday_task_3(message):

    sql.execute(f"SELECT task_3 FROM tuesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE tuesday SET (task_3) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_1(message)

def complete_tuesday_task_4(message):

    sql.execute(f"SELECT task_4 FROM tuesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE tuesday SET (task_4) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_1(message)

def complete_tuesday_task_5(message):

    sql.execute(f"SELECT task_5 FROM tuesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE tuesday SET (task_5) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_1(message)

def complete_tuesday_task_6(message):

    sql.execute(f"SELECT task_6 FROM tuesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE tuesday SET (task_6) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_2(message)

def complete_tuesday_task_7(message):

    sql.execute(f"SELECT task_7 FROM tuesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE tuesday SET (task_7) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_2(message)

def complete_tuesday_task_8(message):

    sql.execute(f"SELECT task_8 FROM tuesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE tuesday SET (task_8) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_2(message)

def complete_tuesday_task_9(message):

    sql.execute(f"SELECT task_9 FROM tuesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE tuesday SET (task_9) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_2(message)

def complete_tuesday_task_10(message):

    sql.execute(f"SELECT task_10 FROM tuesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE tuesday SET (task_10) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_tuesday_tasks_2(message)







#  WEDNESDAY  #

def complete_wednesday_task_1(message):

    sql.execute(f"SELECT task_1 FROM wednesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE wednesday SET (task_1) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_1(message)

def complete_wednesday_task_2(message):

    sql.execute(f"SELECT task_2 FROM wednesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE wednesday SET (task_2) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_1(message)

def complete_wednesday_task_3(message):

    sql.execute(f"SELECT task_3 FROM wednesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE wednesday SET (task_3) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_1(message)

def complete_wednesday_task_4(message):

    sql.execute(f"SELECT task_4 FROM wednesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE wednesday SET (task_4) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_1(message)

def complete_wednesday_task_5(message):

    sql.execute(f"SELECT task_5 FROM wednesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE wednesday SET (task_5) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_1(message)

def complete_wednesday_task_6(message):

    sql.execute(f"SELECT task_6 FROM wednesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE wednesday SET (task_6) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_2(message)

def complete_wednesday_task_7(message):

    sql.execute(f"SELECT task_7 FROM wednesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE wednesday SET (task_7) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_2(message)

def complete_wednesday_task_8(message):

    sql.execute(f"SELECT task_8 FROM wednesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE wednesday SET (task_8) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_2(message)

def complete_wednesday_task_9(message):

    sql.execute(f"SELECT task_9 FROM wednesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE wednesday SET (task_9) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_2(message)

def complete_wednesday_task_10(message):

    sql.execute(f"SELECT task_10 FROM wednesday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE wednesday SET (task_10) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_wednesday_tasks_2(message)







#  THURSDAY  #

def complete_thursday_task_1(message):

    sql.execute(f"SELECT task_1 FROM thursday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE thursday SET (task_1) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_1(message)

def complete_thursday_task_2(message):

    sql.execute(f"SELECT task_2 FROM thursday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE thursday SET (task_2) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_1(message)

def complete_thursday_task_3(message):

    sql.execute(f"SELECT task_3 FROM thursday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE thursday SET (task_3) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_1(message)

def complete_thursday_task_4(message):

    sql.execute(f"SELECT task_4 FROM thursday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE thursday SET (task_4) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_1(message)

def complete_thursday_task_5(message):

    sql.execute(f"SELECT task_5 FROM thursday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE thursday SET (task_5) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_1(message)

def complete_thursday_task_6(message):

    sql.execute(f"SELECT task_6 FROM thursday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE thursday SET (task_6) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_2(message)

def complete_thursday_task_7(message):

    sql.execute(f"SELECT task_7 FROM thursday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE thursday SET (task_7) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_2(message)

def complete_thursday_task_8(message):

    sql.execute(f"SELECT task_8 FROM thursday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE thursday SET (task_8) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_2(message)

def complete_thursday_task_9(message):

    sql.execute(f"SELECT task_9 FROM thursday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE thursday SET (task_9) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_2(message)

def complete_thursday_task_10(message):

    sql.execute(f"SELECT task_10 FROM thursday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE thursday SET (task_10) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_thursday_tasks_2(message)





#  FRIDAY  #

def complete_friday_task_1(message):

    sql.execute(f"SELECT task_1 FROM friday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE friday SET (task_1) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_1(message)

def complete_friday_task_2(message):

    sql.execute(f"SELECT task_2 FROM friday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE friday SET (task_2) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_1(message)

def complete_friday_task_3(message):

    sql.execute(f"SELECT task_3 FROM friday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE friday SET (task_3) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_1(message)

def complete_friday_task_4(message):

    sql.execute(f"SELECT task_4 FROM friday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE friday SET (task_4) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_1(message)

def complete_friday_task_5(message):

    sql.execute(f"SELECT task_5 FROM friday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE friday SET (task_5) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_1(message)

def complete_friday_task_6(message):

    sql.execute(f"SELECT task_6 FROM friday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE friday SET (task_6) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_2(message)

def complete_friday_task_7(message):

    sql.execute(f"SELECT task_7 FROM friday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE friday SET (task_7) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_2(message)

def complete_friday_task_8(message):

    sql.execute(f"SELECT task_8 FROM friday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE friday SET (task_8) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_2(message)

def complete_friday_task_9(message):

    sql.execute(f"SELECT task_9 FROM friday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE friday SET (task_9) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_2(message)

def complete_friday_task_10(message):

    sql.execute(f"SELECT task_10 FROM friday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE friday SET (task_10) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_friday_tasks_2(message)




#  SATURDAY  #

def complete_saturday_task_1(message):

    sql.execute(f"SELECT task_1 FROM saturday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE saturday SET (task_1) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_1(message)

def complete_saturday_task_2(message):

    sql.execute(f"SELECT task_2 FROM saturday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE saturday SET (task_2) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_1(message)

def complete_saturday_task_3(message):

    sql.execute(f"SELECT task_3 FROM saturday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE saturday SET (task_3) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_1(message)

def complete_saturday_task_4(message):

    sql.execute(f"SELECT task_4 FROM saturday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE saturday SET (task_4) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_1(message)

def complete_saturday_task_5(message):

    sql.execute(f"SELECT task_5 FROM saturday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE saturday SET (task_5) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_1(message)

def complete_saturday_task_6(message):

    sql.execute(f"SELECT task_6 FROM saturday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE saturday SET (task_6) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_2(message)

def complete_saturday_task_7(message):

    sql.execute(f"SELECT task_7 FROM saturday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE saturday SET (task_7) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_2(message)

def complete_saturday_task_8(message):

    sql.execute(f"SELECT task_8 FROM saturday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE saturday SET (task_8) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_2(message)

def complete_saturday_task_9(message):

    sql.execute(f"SELECT task_9 FROM saturday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE saturday SET (task_9) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_2(message)

def complete_saturday_task_10(message):

    sql.execute(f"SELECT task_10 FROM saturday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE saturday SET (task_10) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_saturday_tasks_2(message)



#  SUNDAY  #

def complete_sunday_task_1(message):

    sql.execute(f"SELECT task_1 FROM sunday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE sunday SET (task_1) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_1(message)

def complete_sunday_task_2(message):

    sql.execute(f"SELECT task_2 FROM sunday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE sunday SET (task_2) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_1(message)

def complete_sunday_task_3(message):

    sql.execute(f"SELECT task_3 FROM sunday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE sunday SET (task_3) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_1(message)

def complete_sunday_task_4(message):

    sql.execute(f"SELECT task_4 FROM sunday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE sunday SET (task_4) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_1(message)

def complete_sunday_task_5(message):

    sql.execute(f"SELECT task_5 FROM sunday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_1(message)

    else:

        sql.execute(f'''UPDATE sunday SET (task_5) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_1(message)

def complete_sunday_task_6(message):

    sql.execute(f"SELECT task_6 FROM sunday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE sunday SET (task_6) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_2(message)

def complete_sunday_task_7(message):

    sql.execute(f"SELECT task_7 FROM sunday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE sunday SET (task_7) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_2(message)

def complete_sunday_task_8(message):

    sql.execute(f"SELECT task_8 FROM sunday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE sunday SET (task_8) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_2(message)

def complete_sunday_task_9(message):

    sql.execute(f"SELECT task_9 FROM sunday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE sunday SET (task_9) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_2(message)

def complete_sunday_task_10(message):

    sql.execute(f"SELECT task_10 FROM sunday WHERE id = {message.chat.id}")
    task = sql.fetchone()[0]

    if task == "+":

        bot.send_message(message.chat.id, "<b> Нельзя выполнить пустую задачу ❗️ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_2(message)

    else:

        sql.execute(f'''UPDATE sunday SET (task_10) = ('+') WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE tasks_statistics SET {current_month} = {current_month} + 1 WHERE ID = "{message.chat.id}"''')
        db.commit()

        sql.execute(f'''UPDATE user_profile SET active = active + 5 WHERE ID = "{message.chat.id}"''')
        db.commit()

        bot.send_message(message.chat.id, "<b> Вы успешно выполнили задачу   🎉 </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)
        time.sleep(1)

        display_task.display_sunday_tasks_2(message)




