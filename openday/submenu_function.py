from telebot import types


def submenu_function(application):
    for menu_button in application.menulist:
        button = types.InlineKeyboardButton(text=menu_button,
                                            callback_data=menu_button)
        application.keyboard.add(button)
        application.out_text = "Открытие смены"
