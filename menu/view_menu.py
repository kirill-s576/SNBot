# Определяем в какое меню хочет перейти пользователь.
# Проверяем есль ли у него туда доступ
# Отображаем все, что есть в списке.
# На кнопки присваиваем нужные паттерны. openday/open$datastring

from utils.auth import User
from telebot import types
from start import bot
import re


def menu_by_link(message, link, **data):
    user = User(message=message)
    user_full_menulist = user.get_user_menu()
    keyboard = types.InlineKeyboardMarkup()
    link_list = re.findall(r'([^/]*)/', link)
    go_to = link_list[-1]
    print("Полльзователь %s зашел в меню %s" % (user.full_name, go_to))
    open_menulist = user_full_menulist['main']
    for menu_name in link_list:
        if menu_name == "main":
            open_menulist = user_full_menulist['main']
        else:
            try:
                open_menulist = open_menulist[menu_name]
            except:
                print("Доступно только это %s" % open_menulist)

    # Формируем клавиатуру с кнопками
    try:
        for attr in open_menulist:
            if attr not in link:
                button_data = link + attr + "/"
            else:
                button_data = link

            button = types.InlineKeyboardButton(text=attr,
                                                callback_data=button_data)
            keyboard.add(button)
        # Добавляем кнопку "Назад"
        if len(link_list) > 1:
            back_data = "main/"
            back_button = types.InlineKeyboardButton(text="Назад",
                                                     callback_data=back_data)
            keyboard.add(back_button)
        mid = user.get_link()
        if 'new' not in data.items():
            try:
                bot.edit_message_text(link, message.chat.id, message.message_id, reply_markup=keyboard)
            except:
                message = bot.send_message(message.chat.id, link, reply_markup=keyboard)
                for i in range(message.message_id - 40, message.message_id - 1):
                    try:
                        bot.delete_message(message.chat.id, i)
                    except:
                        pass

        else:
            message = bot.send_message(message.chat.id, link, reply_markup=keyboard)
            for i in range(message.message_id-40, message.message_id-1):
                try:
                    bot.delete_message(message.chat.id, i)
                except:
                    pass

        user.set_link(link, message.message_id)

    except:
        print("Тут ничего нет")




