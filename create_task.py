import telebot
import sqlite3
import config
import display_task
import inline_markups

bot = telebot.TeleBot(config.token)

db = sqlite3.connect("productive_master_bot.db", check_same_thread=False)
sql = db.cursor()





#  MONDAY  #

def create_monday_task_1(message):

    sql.execute(f'''UPDATE monday SET (task_1) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_monday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_monday_task_2(message):

    sql.execute(f'''UPDATE monday SET (task_2) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_monday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_monday_task_3(message):

    sql.execute(f'''UPDATE monday SET (task_3) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_monday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_monday_task_4(message):

    sql.execute(f'''UPDATE monday SET (task_4) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_monday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_monday_task_5(message):

    sql.execute(f'''UPDATE monday SET (task_5) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_monday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_monday_task_6(message):

    sql.execute(f'''UPDATE monday SET (task_6) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_monday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_monday_task_7(message):

    sql.execute(f'''UPDATE monday SET (task_7) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_monday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_monday_task_8(message):

    sql.execute(f'''UPDATE monday SET (task_8) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_monday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_monday_task_9(message):

    sql.execute(f'''UPDATE monday SET (task_9) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_monday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_monday_task_10(message):

    sql.execute(f'''UPDATE monday SET (task_10) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_monday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)






#  TUESDAY  #

def create_tuesday_task_1(message):

    sql.execute(f'''UPDATE tuesday SET (task_1) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_tuesday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_tuesday_task_2(message):

    sql.execute(f'''UPDATE tuesday SET (task_2) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_tuesday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_tuesday_task_3(message):

    sql.execute(f'''UPDATE tuesday SET (task_3) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_tuesday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_tuesday_task_4(message):

    sql.execute(f'''UPDATE tuesday SET (task_4) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_tuesday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_tuesday_task_5(message):

    sql.execute(f'''UPDATE tuesday SET (task_5) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_tuesday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_tuesday_task_6(message):

    sql.execute(f'''UPDATE tuesday SET (task_6) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_tuesday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_tuesday_task_7(message):

    sql.execute(f'''UPDATE tuesday SET (task_7) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_tuesday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_tuesday_task_8(message):

    sql.execute(f'''UPDATE tuesday SET (task_8) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_tuesday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_tuesday_task_9(message):

    sql.execute(f'''UPDATE tuesday SET (task_9) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_tuesday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



def create_tuesday_task_10(message):

    sql.execute(f'''UPDATE tuesday SET (task_10) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_tuesday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)





#  WEDNESDAY  #

def create_wednesday_task_1(message):

    sql.execute(f'''UPDATE wednesday SET (task_1) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_wednesday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_wednesday_task_2(message):

    sql.execute(f'''UPDATE wednesday SET (task_2) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_wednesday_tasks_1(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_wednesday_task_3(message):

    sql.execute(f'''UPDATE wednesday SET (task_3) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_wednesday_tasks_1(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_wednesday_task_4(message):

    sql.execute(f'''UPDATE wednesday SET (task_4) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_wednesday_tasks_1(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_wednesday_task_5(message):

    sql.execute(f'''UPDATE wednesday SET (task_5) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_wednesday_tasks_1(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_wednesday_task_6(message):

    sql.execute(f'''UPDATE wednesday SET (task_6) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_wednesday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_wednesday_task_7(message):

    sql.execute(f'''UPDATE wednesday SET (task_7) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_wednesday_tasks_2(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_wednesday_task_8(message):

    sql.execute(f'''UPDATE wednesday SET (task_8) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_wednesday_tasks_2(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_wednesday_task_9(message):

    sql.execute(f'''UPDATE wednesday SET (task_9) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_wednesday_tasks_2(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_wednesday_task_10(message):

    sql.execute(f'''UPDATE wednesday SET (task_10) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_wednesday_tasks_2(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)



#  THURSDAY  #

def create_thursday_task_1(message):

    sql.execute(f'''UPDATE thursday SET (task_1) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_thursday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_thursday_task_2(message):

    sql.execute(f'''UPDATE thursday SET (task_2) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_thursday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_thursday_task_3(message):

    sql.execute(f'''UPDATE thursday SET (task_3) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_thursday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_thursday_task_4(message):

    sql.execute(f'''UPDATE thursday SET (task_4) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_thursday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_thursday_task_5(message):

    sql.execute(f'''UPDATE thursday SET (task_5) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_thursday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_thursday_task_6(message):

    sql.execute(f'''UPDATE thursday SET (task_6) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_thursday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_thursday_task_7(message):

    sql.execute(f'''UPDATE thursday SET (task_7) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_thursday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_thursday_task_8(message):

    sql.execute(f'''UPDATE thursday SET (task_8) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_thursday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_thursday_task_9(message):

    sql.execute(f'''UPDATE thursday SET (task_9) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_thursday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_thursday_task_10(message):

    sql.execute(f'''UPDATE thursday SET (task_10) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_thursday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)





#  FRIDAY  #

def create_friday_task_1(message):

    sql.execute(f'''UPDATE friday SET (task_1) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_friday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)

    
def create_friday_task_2(message):

    sql.execute(f'''UPDATE friday SET (task_2) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_friday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_friday_task_3(message):

    sql.execute(f'''UPDATE friday SET (task_3) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_friday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_friday_task_4(message):

    sql.execute(f'''UPDATE friday SET (task_4) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_friday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_friday_task_5(message):

    sql.execute(f'''UPDATE friday SET (task_5) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_friday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_friday_task_6(message):

    sql.execute(f'''UPDATE friday SET (task_6) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_friday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)

    
def create_friday_task_7(message):

    sql.execute(f'''UPDATE friday SET (task_7) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_friday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_friday_task_8(message):

    sql.execute(f'''UPDATE friday SET (task_8) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_friday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_friday_task_9(message):

    sql.execute(f'''UPDATE friday SET (task_9) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_friday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_friday_task_10(message):

    sql.execute(f'''UPDATE friday SET (task_10) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_friday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)





#  SATURDAY  #

def create_saturday_task_1(message):

    sql.execute(f'''UPDATE saturday SET (task_1) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_saturday_tasks_1(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)

    


def create_saturday_task_2(message):

    sql.execute(f'''UPDATE saturday SET (task_2) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_saturday_tasks_1(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_saturday_task_3(message):

    sql.execute(f'''UPDATE saturday SET (task_3) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_saturday_tasks_1(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_saturday_task_4(message):

    sql.execute(f'''UPDATE saturday SET (task_4) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_saturday_tasks_1(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_saturday_task_5(message):

    sql.execute(f'''UPDATE saturday SET (task_5) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_saturday_tasks_1(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_saturday_task_6(message):

    sql.execute(f'''UPDATE saturday SET (task_6) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_saturday_tasks_2(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)

    


def create_saturday_task_7(message):

    sql.execute(f'''UPDATE saturday SET (task_7) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_saturday_tasks_2(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_saturday_task_8(message):

    sql.execute(f'''UPDATE saturday SET (task_8) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_saturday_tasks_2(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_saturday_task_9(message):

    sql.execute(f'''UPDATE saturday SET (task_9) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_saturday_tasks_2(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_saturday_task_10(message):

    sql.execute(f'''UPDATE saturday SET (task_10) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_saturday_tasks_2(message)
    
    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)





#  SUNDAY  #

def create_sunday_task_1(message):

    sql.execute(f'''UPDATE sunday SET (task_1) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_sunday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)

    
def create_sunday_task_2(message):

    sql.execute(f'''UPDATE sunday SET (task_2) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_sunday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_sunday_task_3(message):

    sql.execute(f'''UPDATE sunday SET (task_3) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_sunday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_sunday_task_4(message):

    sql.execute(f'''UPDATE sunday SET (task_4) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_sunday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_sunday_task_5(message):

    sql.execute(f'''UPDATE sunday SET (task_5) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_sunday_tasks_1(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_sunday_task_6(message):

    sql.execute(f'''UPDATE sunday SET (task_6) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_sunday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)

    
def create_sunday_task_7(message):

    sql.execute(f'''UPDATE sunday SET (task_7) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_sunday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_sunday_task_8(message):

    sql.execute(f'''UPDATE sunday SET (task_8) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_sunday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_sunday_task_9(message):

    sql.execute(f'''UPDATE sunday SET (task_9) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_sunday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)


def create_sunday_task_10(message):

    sql.execute(f'''UPDATE sunday SET (task_10) = ('{message.text}') WHERE ID = "{message.chat.id}"''')
    db.commit()

    display_task.display_sunday_tasks_2(message)

    bot.send_message(message.chat.id, "<b> Ваша задача успешно добавлена  ✅ </b>", parse_mode="html", reply_markup=inline_markups.hide_inline)













