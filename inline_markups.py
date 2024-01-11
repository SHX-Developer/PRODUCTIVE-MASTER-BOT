from telebot import types


#  TASKS  #

day_inline = types.InlineKeyboardMarkup(row_width=1)
monday = types.InlineKeyboardButton(text="Понедельник", callback_data="monday")
tuesday = types.InlineKeyboardButton(text="Вторник", callback_data="tuesday")
wednesday = types.InlineKeyboardButton(text="Среда", callback_data="wednesday")
thursday = types.InlineKeyboardButton(text="Четверг", callback_data="thursday")
friday = types.InlineKeyboardButton(text="Пятница", callback_data="friday")
saturday = types.InlineKeyboardButton(text="Суббота", callback_data="saturday")
sunday = types.InlineKeyboardButton(text="Воскресенье", callback_data="sunday")
day_inline.add(monday, tuesday, wednesday, thursday, friday, saturday, sunday)


#  NOTES  #

notes_inline = types.InlineKeyboardMarkup(row_width=1)
write_notes = types.InlineKeyboardButton(text="Записать", callback_data="write_notes")
clear_notes = types.InlineKeyboardButton(text="Очистить", callback_data="clear_notes")
notes_inline.add(write_notes, clear_notes)




#  CREATE CARD  #

create_balance_inline = types.InlineKeyboardMarkup(row_width=1)
create_card = types.InlineKeyboardButton(text="Создать карту", callback_data="create_card")
create_balance_inline.add(create_card)

#  CURRENCY  #

currency_inline = types.InlineKeyboardMarkup(row_width=3)
usd = types.InlineKeyboardButton(text="USD", callback_data="USD")
rub = types.InlineKeyboardButton(text="RUB", callback_data="RUB")
uzs = types.InlineKeyboardButton(text="UZS", callback_data="UZS")
currency_inline.add(usd, rub, uzs)



#  FINANCE  #

finance_inline = types.InlineKeyboardMarkup()

finance_inline.row(types.InlineKeyboardButton(text="Баланс", callback_data="balance"))

finance_inline.row(types.InlineKeyboardButton(text="Добавить", callback_data="add_finance"),
                   types.InlineKeyboardButton(text="Отнять", callback_data="waste_finance"))

finance_inline.row(types.InlineKeyboardButton(text="Доходы", callback_data="income"),
                   types.InlineKeyboardButton(text="Расходы", callback_data="outcome"))



#  BALANCE HIDED  #

balance_inline_1 = types.InlineKeyboardMarkup(row_width=1)
show_balance = types.InlineKeyboardButton(text="Показать баланс", callback_data="show_balance")
edit_balance = types.InlineKeyboardButton(text="Изменить баланс", callback_data="edit_balance")
back_balance = types.InlineKeyboardButton(text="Назад", callback_data="back_finance")
balance_inline_1.add(show_balance, edit_balance, back_balance)

#  BALANCE SHOWED  #

balance_inline_2 = types.InlineKeyboardMarkup(row_width=1)
hide_balance = types.InlineKeyboardButton(text="Скрыть баланс", callback_data="hide_balance")
edit_balance = types.InlineKeyboardButton(text="Изменить баланс", callback_data="edit_balance")
back_finance = types.InlineKeyboardButton(text="Назад", callback_data="back_finance")
balance_inline_2.add(hide_balance, edit_balance, back_finance)



#  BACK FINANCE  #

back_finance_inline = types.InlineKeyboardMarkup(row_width=1)
back_finance = types.InlineKeyboardButton(text="Назад", callback_data="back_finance")
back_finance_inline.add(back_finance)





#  HISTORY  #

history_inline = types.InlineKeyboardMarkup(row_width=2)
income_history = types.InlineKeyboardButton(text="История доходов", callback_data="income_history")
outcome_history = types.InlineKeyboardButton(text="История расходов", callback_data="outcome_history")
history_inline.add(income_history, outcome_history)





#  STATISTICS MENU  #

statistics_inline = types.InlineKeyboardMarkup(row_width=1)
month_statistics = types.InlineKeyboardButton(text="Подробная статистика", callback_data="month_statistics")
statistics_inline.add(month_statistics)

#  STATISTICS MONTH  #

month_statistics_inline = types.InlineKeyboardMarkup()
month_statistics_inline.row(types.InlineKeyboardButton(text="За всё время", callback_data="all_time_statistics"))

month_statistics_inline.row(types.InlineKeyboardButton(text="Январь", callback_data="statistics_january"),
                            types.InlineKeyboardButton(text="Февраль", callback_data="statistics_february"),
                            types.InlineKeyboardButton(text="Март", callback_data="statistics_march"),
                            types.InlineKeyboardButton(text="Апрель", callback_data="statistics_april"))

month_statistics_inline.row(types.InlineKeyboardButton(text="Май", callback_data="statistics_may"),
                            types.InlineKeyboardButton(text="Июнь", callback_data="statistics_june"),
                            types.InlineKeyboardButton(text="Июль", callback_data="statistics_july"),
                            types.InlineKeyboardButton(text="Август", callback_data="statistics_august"))

month_statistics_inline.row(types.InlineKeyboardButton(text="Сентябрь", callback_data="statistics_september"),
                            types.InlineKeyboardButton(text="Октябрь", callback_data="statistics_october"),
                            types.InlineKeyboardButton(text="Ноябрь", callback_data="statistics_november"),
                            types.InlineKeyboardButton(text="Декабрь", callback_data="statistics_december"))

month_statistics_inline.row(types.InlineKeyboardButton(text="Назад", callback_data="back_statistics"))




#  PROFILE  #

profile_inline = types.InlineKeyboardMarkup(row_width=1)
status = types.InlineKeyboardButton(text="Статус", callback_data="status")
active = types.InlineKeyboardButton(text="Активность", callback_data="active")
profile_inline.add(status, active)




#  DELETE MESSAGE  #

hide_inline = types.InlineKeyboardMarkup(row_width=1)
hide_message = types.InlineKeyboardButton(text="Скрыть сообщение", callback_data="hide_message")
hide_inline.add(hide_message)



#  CANCEL  #

cancel_inline = types.InlineKeyboardMarkup(row_width=1)
cancel = types.InlineKeyboardButton(text="Отменить", callback_data="cancel")
cancel_inline.add(cancel)


