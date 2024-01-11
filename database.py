import sqlite3
import datetime


db = sqlite3.connect("productive_master_bot.db", check_same_thread=False)
sql = db.cursor()

current_date = datetime.datetime.now().date()



def add_start(message):

    #  INSERT USER DATA  #

    sql.execute('''INSERT INTO user_access (id, username, firstname, lastname, date) VALUES (?, ?, ?, ?, ?)''',
    (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), current_date))
    db.commit()

    #  INSERT TASKS  #

    sql.execute('''INSERT INTO monday (id, task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    (str(message.chat.id), "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"))
    db.commit()

    sql.execute('''INSERT INTO tuesday (id, task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    (str(message.chat.id), "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"))
    db.commit()

    sql.execute('''INSERT INTO wednesday (id, task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    (str(message.chat.id), "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"))
    db.commit()

    sql.execute('''INSERT INTO thursday (id, task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    (str(message.chat.id), "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"))
    db.commit()

    sql.execute('''INSERT INTO friday (id, task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    (str(message.chat.id), "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"))
    db.commit()

    sql.execute('''INSERT INTO saturday (id, task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    (str(message.chat.id), "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"))
    db.commit()

    sql.execute('''INSERT INTO sunday (id, task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    (str(message.chat.id), "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"))
    db.commit()

    #  INSERT PROFILE  #

    sql.execute('''INSERT INTO user_profile (id, date, active) VALUES (?, ?, ?, ?)''',
    (str(message.chat.id), current_date, "Новичок", 0))
    db.commit()

    #  INSERT STATISTICS  #

    sql.execute('''INSERT INTO user_statistics (id, tasks, income, outcome) VALUES (?, ?, ?, ?)''',
    (str(message.chat.id), 0, 0, 0))
    db.commit()

    #  INSERT FINANCE  #

    sql.execute('''INSERT INTO user_finance (id, status, currency, balance) VALUES (?, ?, ?, ?)''',
    (str(message.chat.id), "No", "[валюта не указана]", 0))
    db.commit()

    #  INSERT  MONTH  #

    sql.execute('''INSERT INTO finance_statistics (id, January, February, March, April, May, June, July, August, September, October, November, December) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    (str(message.chat.id), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    db.commit()

    sql.execute('''INSERT INTO income_statistics (id, January, February, March, April, May, June, July, August, September, October, November, December) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    (str(message.chat.id), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    db.commit()

    sql.execute('''INSERT INTO outcome_statistics (id, January, February, March, April, May, June, July, August, September, October, November, December) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    (str(message.chat.id), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    db.commit()

    sql.execute('''INSERT INTO tasks_statistics (id, January, February, March, April, May, June, July, August, September, October, November, December) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    (str(message.chat.id), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    db.commit()