from telebot import types, telebot
import sqlite3
import config

bot = telebot.TeleBot(config.token)

db = sqlite3.connect("productive_master_bot.db", check_same_thread=False)
sql = db.cursor()





#  MONDAY  #

def edit_monday_inline_1(call):

    sql.execute(f'''SELECT task_1 FROM monday WHERE ID = {call.message.chat.id}''')
    task_1 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_2 FROM monday WHERE ID = {call.message.chat.id}''')
    task_2 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_3 FROM monday WHERE ID = {call.message.chat.id}''')
    task_3 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_4 FROM monday WHERE ID = {call.message.chat.id}''')
    task_4 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_5 FROM monday WHERE ID = {call.message.chat.id}''')
    task_5 = sql.fetchone()[0]

    tasks_inline = types.InlineKeyboardMarkup()
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_1}", callback_data="add_monday_task_1"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_monday_task_1"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_monday_task_1"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_2}", callback_data="add_monday_task_2"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_monday_task_2"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_monday_task_2"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_3}", callback_data="add_monday_task_3"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_monday_task_3"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_monday_task_3"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_4}", callback_data="add_monday_task_4"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_monday_task_4"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_monday_task_4"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_5}", callback_data="add_monday_task_5"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_monday_task_5"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_monday_task_5"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Следующая страница >>>", callback_data="next_monday_tasks"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Назад", callback_data="back_week"))

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text="<b> Ваши задачи на понедельник: </b>", 
                          parse_mode="html", reply_markup=tasks_inline)


def edit_monday_inline_2(call):

    sql.execute(f'''SELECT task_6 FROM monday WHERE ID = {call.message.chat.id}''')
    task_6= sql.fetchone()[0]

    sql.execute(f'''SELECT task_7 FROM monday WHERE ID = {call.message.chat.id}''')
    task_7 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_8 FROM monday WHERE ID = {call.message.chat.id}''')
    task_8 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_9 FROM monday WHERE ID = {call.message.chat.id}''')
    task_9 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_10 FROM monday WHERE ID = {call.message.chat.id}''')
    task_10 = sql.fetchone()[0]

    tasks_inline = types.InlineKeyboardMarkup() 
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_6}", callback_data="add_monday_task_6"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_monday_task_6"),
                            types.InlineKeyboardButton(text="❌", callback_data="delete_monday_task_6"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_7}", callback_data="add_monday_task_7"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_monday_task_7"),
                            types.InlineKeyboardButton(text="❌", callback_data="delete_monday_task_7"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_8}", callback_data="add_monday_task_8"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_monday_task_8"),
                            types.InlineKeyboardButton(text="❌", callback_data="delete_monday_task_8"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_9}", callback_data="add_monday_task_9"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_monday_task_9"),
                            types.InlineKeyboardButton(text="❌", callback_data="delete_monday_task_9"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_10}", callback_data="add_monday_task_10"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_monday_task_10"),
                            types.InlineKeyboardButton(text="❌", callback_data="delete_monday_task_10"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"<<<  Предыдущая страница", callback_data="previous_monday_tasks"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Назад", callback_data="back_week"))

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text="<b> Ваши задачи на понедельник: </b>", 
                          parse_mode="html", reply_markup=tasks_inline)





#  TUESDAY  #

def edit_tuesday_inline_1(call):

    sql.execute(f'''SELECT task_1 FROM tuesday WHERE ID = {call.message.chat.id}''')
    task_1 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_2 FROM tuesday WHERE ID = {call.message.chat.id}''')
    task_2 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_3 FROM tuesday WHERE ID = {call.message.chat.id}''')
    task_3 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_4 FROM tuesday WHERE ID = {call.message.chat.id}''')
    task_4 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_5 FROM tuesday WHERE ID = {call.message.chat.id}''')
    task_5 = sql.fetchone()[0]

    tasks_inline = types.InlineKeyboardMarkup()
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_1}", callback_data="add_tuesday_task_1"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_tuesday_task_1"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_tuesday_task_1"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_2}", callback_data="add_tuesday_task_2"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_tuesday_task_2"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_tuesday_task_2"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_3}", callback_data="add_tuesday_task_3"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_tuesday_task_3"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_tuesday_task_3"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_4}", callback_data="add_tuesday_task_4"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_tuesday_task_4"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_tuesday_task_4"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_5}", callback_data="add_tuesday_task_5"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_tuesday_task_5"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_tuesday_task_5"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Следующая страница >>>", callback_data="next_tuesday_tasks"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Назад", callback_data="back_week"))

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text="<b> Ваши задачи на вторник: </b>", 
                          parse_mode="html", reply_markup=tasks_inline)


def edit_tuesday_inline_2(call):

    sql.execute(f'''SELECT task_6 FROM tuesday WHERE ID = {call.message.chat.id}''')
    task_6= sql.fetchone()[0]

    sql.execute(f'''SELECT task_7 FROM tuesday WHERE ID = {call.message.chat.id}''')
    task_7 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_8 FROM tuesday WHERE ID = {call.message.chat.id}''')
    task_8 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_9 FROM tuesday WHERE ID = {call.message.chat.id}''')
    task_9 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_10 FROM tuesday WHERE ID = {call.message.chat.id}''')
    task_10 = sql.fetchone()[0]

    tasks_inline = types.InlineKeyboardMarkup() 
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_6}", callback_data="add_tuesday_task_6"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_tuesday_task_6"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_tuesday_task_6"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_7}", callback_data="add_tuesday_task_7"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_tuesday_task_7"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_tuesday_task_7"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_8}", callback_data="add_tuesday_task_8"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_tuesday_task_8"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_tuesday_task_8"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_9}", callback_data="add_tuesday_task_9"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_tuesday_task_9"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_tuesday_task_9"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_10}", callback_data="add_tuesday_task_10"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_tuesday_task_10"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_tuesday_task_10"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"<<<  Предыдущая страница", callback_data="previous_tuesday_tasks"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Назад", callback_data="back_week"))

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text="<b> Ваши задачи на вторник: </b>", 
                          parse_mode="html", reply_markup=tasks_inline)



#  WEDNESDAY  #

def edit_wednesday_inline_1(call):

    sql.execute(f'''SELECT task_1 FROM wednesday WHERE ID = {call.message.chat.id}''')
    task_1 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_2 FROM wednesday WHERE ID = {call.message.chat.id}''')
    task_2 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_3 FROM wednesday WHERE ID = {call.message.chat.id}''')
    task_3 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_4 FROM wednesday WHERE ID = {call.message.chat.id}''')
    task_4 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_5 FROM wednesday WHERE ID = {call.message.chat.id}''')
    task_5 = sql.fetchone()[0]

    tasks_inline = types.InlineKeyboardMarkup()
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_1}", callback_data="add_wednesday_task_1"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_wednesday_task_1"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_wednesday_task_1"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_2}", callback_data="add_wednesday_task_2"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_wednesday_task_2"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_wednesday_task_2"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_3}", callback_data="add_wednesday_task_3"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_wednesday_task_3"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_wednesday_task_3"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_4}", callback_data="add_wednesday_task_4"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_wednesday_task_4"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_wednesday_task_4"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_5}", callback_data="add_wednesday_task_5"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_wednesday_task_5"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_wednesday_task_5"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Следующая страница >>>", callback_data="next_wednesday_tasks"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Назад", callback_data="back_week"))

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text="<b> Ваши задачи на среду: </b>", 
                          parse_mode="html", reply_markup=tasks_inline)


def edit_wednesday_inline_2(call):

    sql.execute(f'''SELECT task_6 FROM wednesday WHERE ID = {call.message.chat.id}''')
    task_6= sql.fetchone()[0]

    sql.execute(f'''SELECT task_7 FROM wednesday WHERE ID = {call.message.chat.id}''')
    task_7 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_8 FROM wednesday WHERE ID = {call.message.chat.id}''')
    task_8 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_9 FROM wednesday WHERE ID = {call.message.chat.id}''')
    task_9 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_10 FROM wednesday WHERE ID = {call.message.chat.id}''')
    task_10 = sql.fetchone()[0]

    tasks_inline = types.InlineKeyboardMarkup() 
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_6}", callback_data="add_wednesday_task_6"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_wednesday_task_6"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_wednesday_task_6"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_7}", callback_data="add_wednesday_task_7"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_wednesday_task_7"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_wednesday_task_7"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_8}", callback_data="add_wednesday_task_8"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_wednesday_task_8"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_wednesday_task_8"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_9}", callback_data="add_wednesday_task_9"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_wednesday_task_9"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_wednesday_task_9"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_10}", callback_data="add_wednesday_task_10"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_wednesday_task_10"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_wednesday_task_10"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"<<<  Предыдущая страница", callback_data="previous_wednesday_tasks"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Назад", callback_data="back_week"))

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text="<b> Ваши задачи на среду: </b>", 
                          parse_mode="html", reply_markup=tasks_inline)




#  THURSDAY  #

def edit_thursday_inline_1(call):

    sql.execute(f'''SELECT task_1 FROM thursday WHERE ID = {call.message.chat.id}''')
    task_1 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_2 FROM thursday WHERE ID = {call.message.chat.id}''')
    task_2 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_3 FROM thursday WHERE ID = {call.message.chat.id}''')
    task_3 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_4 FROM thursday WHERE ID = {call.message.chat.id}''')
    task_4 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_5 FROM thursday WHERE ID = {call.message.chat.id}''')
    task_5 = sql.fetchone()[0]

    tasks_inline = types.InlineKeyboardMarkup()
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_1}", callback_data="add_thursday_task_1"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_thursday_task_1"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_thursday_task_1"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_2}", callback_data="add_thursday_task_2"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_thursday_task_2"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_thursday_task_2"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_3}", callback_data="add_thursday_task_3"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_thursday_task_3"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_thursday_task_3"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_4}", callback_data="add_thursday_task_4"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_thursday_task_4"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_thursday_task_4"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_5}", callback_data="add_thursday_task_5"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_thursday_task_5"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_thursday_task_5"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Следующая страница >>>", callback_data="next_thursday_tasks"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Назад", callback_data="back_week"))

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text="<b> Ваши задачи на четверг: </b>", 
                          parse_mode="html", reply_markup=tasks_inline)


def edit_thursday_inline_2(call):

    sql.execute(f'''SELECT task_6 FROM thursday WHERE ID = {call.message.chat.id}''')
    task_6= sql.fetchone()[0]

    sql.execute(f'''SELECT task_7 FROM thursday WHERE ID = {call.message.chat.id}''')
    task_7 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_8 FROM thursday WHERE ID = {call.message.chat.id}''')
    task_8 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_9 FROM thursday WHERE ID = {call.message.chat.id}''')
    task_9 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_10 FROM thursday WHERE ID = {call.message.chat.id}''')
    task_10 = sql.fetchone()[0]

    tasks_inline = types.InlineKeyboardMarkup() 
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_6}", callback_data="add_thursday_task_6"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_thursday_task_6"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_thursday_task_6"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_7}", callback_data="add_thursday_task_7"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_thursday_task_7"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_thursday_task_7"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_8}", callback_data="add_thursday_task_8"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_thursday_task_8"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_thursday_task_8"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_9}", callback_data="add_thursday_task_9"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_thursday_task_9"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_thursday_task_9"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_10}", callback_data="add_thursday_task_10"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_thursday_task_10"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_thursday_task_10"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"<<<  Предыдущая страница", callback_data="previous_thursday_tasks"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Назад", callback_data="back_week"))

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text="<b> Ваши задачи на четверг: </b>", 
                          parse_mode="html", reply_markup=tasks_inline)



#  FRIDAY  #

def edit_friday_inline_1(call):

    sql.execute(f'''SELECT task_1 FROM friday WHERE ID = {call.message.chat.id}''')
    task_1 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_2 FROM friday WHERE ID = {call.message.chat.id}''')
    task_2 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_3 FROM friday WHERE ID = {call.message.chat.id}''')
    task_3 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_4 FROM friday WHERE ID = {call.message.chat.id}''')
    task_4 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_5 FROM friday WHERE ID = {call.message.chat.id}''')
    task_5 = sql.fetchone()[0]

    tasks_inline = types.InlineKeyboardMarkup()
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_1}", callback_data="add_friday_task_1"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_friday_task_1"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_friday_task_1"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_2}", callback_data="add_friday_task_2"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_friday_task_2"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_friday_task_2"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_3}", callback_data="add_friday_task_3"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_friday_task_3"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_friday_task_3"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_4}", callback_data="add_friday_task_4"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_friday_task_4"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_friday_task_4"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_5}", callback_data="add_friday_task_5"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_friday_task_5"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_friday_task_5"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Следующая страница >>>", callback_data="next_friday_tasks"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Назад", callback_data="back_week"))

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text="<b> Ваши задачи на пятницу: </b>", 
                          parse_mode="html", reply_markup=tasks_inline)


def edit_friday_inline_2(call):

    sql.execute(f'''SELECT task_6 FROM friday WHERE ID = {call.message.chat.id}''')
    task_6= sql.fetchone()[0]

    sql.execute(f'''SELECT task_7 FROM friday WHERE ID = {call.message.chat.id}''')
    task_7 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_8 FROM friday WHERE ID = {call.message.chat.id}''')
    task_8 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_9 FROM friday WHERE ID = {call.message.chat.id}''')
    task_9 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_10 FROM friday WHERE ID = {call.message.chat.id}''')
    task_10 = sql.fetchone()[0]

    tasks_inline = types.InlineKeyboardMarkup() 
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_6}", callback_data="add_friday_task_6"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_friday_task_6"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_friday_task_6"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_7}", callback_data="add_friday_task_7"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_friday_task_7"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_friday_task_7"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_8}", callback_data="add_friday_task_8"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_friday_task_8"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_friday_task_8"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_9}", callback_data="add_friday_task_9"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_friday_task_9"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete__task_9"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_10}", callback_data="add_friday_task_10"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_friday_task_10"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_friday_task_10"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"<<<  Предыдущая страница", callback_data="previous_friday_tasks"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Назад", callback_data="back_week"))

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text="<b> Ваши задачи на пятницу: </b>", 
                          parse_mode="html", reply_markup=tasks_inline)



#  SATURDAY  #

def edit_saturday_inline_1(call):

    sql.execute(f'''SELECT task_1 FROM saturday WHERE ID = {call.message.chat.id}''')
    task_1 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_2 FROM saturday WHERE ID = {call.message.chat.id}''')
    task_2 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_3 FROM saturday WHERE ID = {call.message.chat.id}''')
    task_3 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_4 FROM saturday WHERE ID = {call.message.chat.id}''')
    task_4 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_5 FROM saturday WHERE ID = {call.message.chat.id}''')
    task_5 = sql.fetchone()[0]

    tasks_inline = types.InlineKeyboardMarkup()
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_1}", callback_data="add_saturday_task_1"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_saturday_task_1"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_saturday_task_1"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_2}", callback_data="add_saturday_task_2"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_saturday_task_2"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_saturday_task_2"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_3}", callback_data="add_saturday_task_3"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_saturday_task_3"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_saturday_task_3"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_4}", callback_data="add_saturday_task_4"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_saturday_task_4"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_saturday_task_4"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_5}", callback_data="add_saturday_task_5"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_saturday_task_5"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_saturday_task_5"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Следующая страница >>>", callback_data="next_saturday_tasks"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Назад", callback_data="back_week"))

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text="<b> Ваши задачи на субботу: </b>", 
                          parse_mode="html", reply_markup=tasks_inline)


def edit_saturday_inline_2(call):

    sql.execute(f'''SELECT task_6 FROM saturday WHERE ID = {call.message.chat.id}''')
    task_6= sql.fetchone()[0]

    sql.execute(f'''SELECT task_7 FROM saturday WHERE ID = {call.message.chat.id}''')
    task_7 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_8 FROM saturday WHERE ID = {call.message.chat.id}''')
    task_8 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_9 FROM saturday WHERE ID = {call.message.chat.id}''')
    task_9 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_10 FROM saturday WHERE ID = {call.message.chat.id}''')
    task_10 = sql.fetchone()[0]

    tasks_inline = types.InlineKeyboardMarkup() 
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_6}", callback_data="add_saturday_task_6"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_saturday_task_6"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_saturday_task_6"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_7}", callback_data="add_saturday_task_7"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_saturday_task_7"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_saturday_task_7"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_8}", callback_data="add_saturday_task_8"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_saturday_task_8"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_saturday_task_8"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_9}", callback_data="add_saturday_task_9"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_saturday_task_9"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_saturday_task_9"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_10}", callback_data="add_saturday_task_10"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_saturday_task_10"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_saturday_task_10"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"<<<  Предыдущая страница", callback_data="previous_saturday_tasks"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Назад", callback_data="back_week"))

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text="<b> Ваши задачи на субботу: </b>", 
                          parse_mode="html", reply_markup=tasks_inline)


#  SUNDAY  #

def edit_sunday_inline_1(call):

    sql.execute(f'''SELECT task_1 FROM sunday WHERE ID = {call.message.chat.id}''')
    task_1 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_2 FROM sunday WHERE ID = {call.message.chat.id}''')
    task_2 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_3 FROM sunday WHERE ID = {call.message.chat.id}''')
    task_3 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_4 FROM sunday WHERE ID = {call.message.chat.id}''')
    task_4 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_5 FROM sunday WHERE ID = {call.message.chat.id}''')
    task_5 = sql.fetchone()[0]

    tasks_inline = types.InlineKeyboardMarkup()
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_1}", callback_data="add_sunday_task_1"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_sunday_task_1"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_sunday_task_1"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_2}", callback_data="add_sunday_task_2"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_sunday_task_2"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_sunday_task_2"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_3}", callback_data="add_sunday_task_3"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_sunday_task_3"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_sunday_task_3"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_4}", callback_data="add_sunday_task_4"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_sunday_task_4"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_sunday_task_4"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_5}", callback_data="add_sunday_task_5"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_sunday_task_5"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_sunday_task_5"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Следующая страница >>>", callback_data="next_sunday_tasks"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Назад", callback_data="back_week"))

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text="<b> Ваши задачи на воскресенье: </b>", 
                          parse_mode="html", reply_markup=tasks_inline)


def edit_sunday_inline_2(call):

    sql.execute(f'''SELECT task_6 FROM sunday WHERE ID = {call.message.chat.id}''')
    task_6= sql.fetchone()[0]

    sql.execute(f'''SELECT task_7 FROM sunday WHERE ID = {call.message.chat.id}''')
    task_7 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_8 FROM sunday WHERE ID = {call.message.chat.id}''')
    task_8 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_9 FROM sunday WHERE ID = {call.message.chat.id}''')
    task_9 = sql.fetchone()[0]

    sql.execute(f'''SELECT task_10 FROM sunday WHERE ID = {call.message.chat.id}''')
    task_10 = sql.fetchone()[0]

    tasks_inline = types.InlineKeyboardMarkup() 
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_6}", callback_data="add_sunday_task_6"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_sunday_task_6"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_sunday_task_6"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_7}", callback_data="add_sunday_task_7"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_sunday_task_7"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_sunday_task_7"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_8}", callback_data="add_sunday_task_8"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_sunday_task_8"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_sunday_task_8"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_9}", callback_data="add_sunday_task_9"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_sunday_task_9"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_sunday_task_9"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"{task_10}", callback_data="add_sunday_task_10"))
    tasks_inline.row(types.InlineKeyboardButton(text="✅", callback_data="complete_sunday_task_10"),
                     types.InlineKeyboardButton(text="❌", callback_data="delete_sunday_task_10"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"<<<  Предыдущая страница", callback_data="previous_sunday_tasks"))
    tasks_inline.row(types.InlineKeyboardButton(text=f"Назад", callback_data="back_week"))

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text="<b> Ваши задачи на воскресенье: </b>", 
                          parse_mode="html", reply_markup=tasks_inline)
    































