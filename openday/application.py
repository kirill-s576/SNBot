from openday import submenu_function
from utils.auth import User
from utils.database import Sql
import datetime
from telebot import types
from utils.memory import Memory

# Класс приложения открытия смены.
class Application(object):
    def __init__(self, request):
        self.request = request
        self.for_users = ['admin']
        self.menulist = ['Открыть смену', 'Закрыть смену', 'Статистика', 'Главное меню']
        print("Запущено приложение открытия смены")
        # Пример memory {"app":"openday", "subapp":"Открыть смену", "data":{"name":"Филимонов", .....}}
        # Кодирование JSON
        # encoded_hand = json.dumps(blackjack_hand)
        # decoded_hand = json.loads(encoded_hand)

        self.out_text = ""
        self.keyboard = types.InlineKeyboardMarkup()
        self.memory = Memory(self.request.user).object
        self.app = "openday"


        # call.message.json['reply_markup']['inline_keyboard'] - входящая клавиатура сообщения. Если это коллбэк.

    def out_result(self):
        print(self.memory)
        try:
            app = self.memory["subapp"]
            print(app)
        except:
            app = self.request.call.data

        if "Главное меню" in app:
            self.app = "menu"
        elif "Открыть смену" in app:
            self.open_day()
        elif "Закрыть смену" in app:
            self.close_day()
        elif "Статистика" in app:
            self.stat()
        else:
            self.submenu()
            # Отобразить пункты меню

    def submenu(self):
        # Формирем сообщение меню приложения.
        from openday.submenu_function import submenu_function
        submenu_function(self)
        return ''

    def open_day(self):
        from openday.open_day_function import open_day_function
        return open_day_function(self)

    def close_day(self):
        from openday.close_day_function import close_day_function
        return close_day_function(self)

    def stat(self):

        return ''

    def sql_insert_new_day(self):
        query = Sql('snb_opentime').insert(user_id=self.request.user.user_id, datetime_open=datetime.datetime.now())
        query.run()




