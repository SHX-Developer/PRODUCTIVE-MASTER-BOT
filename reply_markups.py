import telebot



menu_button = telebot.types.ReplyKeyboardMarkup(True)
menu_button.row("📊  Статистика")
menu_button.row("📝  Задачи", "💸  Финанс")
menu_button.row("📔  Заметки", "📁  История")
menu_button.row("👤  Профиль")


create_balance_button = telebot.types.ReplyKeyboardMarkup(True)
create_balance_button.row("Создать карту")
create_balance_button.row("Главное меню")

finance_button = telebot.types.ReplyKeyboardMarkup(True)
finance_button.row("Баланс")
finance_button.row("Добавить", "Отнять")
finance_button.row("Расход", "Доход")