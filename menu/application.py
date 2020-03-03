from telebot import types

# Класс приложения открытия смены.
class Application(object):
    def __init__(self, request):
        self.request = request
        self.for_users = ['admin']
        self.menulist = ['Открытие смены', 'Акции', 'Рассрочка', 'Управление']

        # Пример memory {"app":"openday", "subapp":"Открыть смену", "data":{"name":"Филимонов", .....}}
        # Кодирование JSON
        # encoded_hand = json.dumps(blackjack_hand)
        # decoded_hand = json.loads(encoded_hand)

        self.out_text = ""
        self.keyboard = types.InlineKeyboardMarkup()
        self.memory = self.request.user.memory
        self.app = "menu"
        # call.message.json['reply_markup']['inline_keyboard'] - входящая клавиатура сообщения. Если это коллбэк.

    def out_result(self):

        if self.request.call is not None:
            if "Открытие смены" in self.request.call.data:
                self.app = "openday"
            elif "Главное меню" in self.request.call.data:
                # Отобразить пункты меню
                self.submenu()
        # if self.request.user.memory == "":
        elif self.request.message.text == "Меню":
            # Отобразить пункты меню
            self.submenu()


    def submenu(self):
        # Формирем сообщение меню приложения.
        from menu.submenu_function import submenu_function
        submenu_function(self)
        return ''

