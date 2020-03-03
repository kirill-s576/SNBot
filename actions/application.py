from openday import submenu_function
from utils.auth import User
from utils.database import Sql
import datetime
from telebot import types

# Класс приложения открытия смены.
class Application(object):
    def __init__(self, request):
        self.request = request
        # self.for_users = ['admin']
        self.menulist = ['Товар дня-недели', 'Все сегодня', 'Главное меню']

        self.out_text = ""
        self.keyboard = types.InlineKeyboardMarkup()
        self.memory = self.request.user.memory
        self.app = "app_name"  # !!!!!!!!!!!!!


    def out_result(self):

        if ("Главное меню" in self.request.user.memory) or \
                ("Главное меню" in self.request.call.data):
            self.app = "menu"
        # elif ("Открыть смену" in self.request.user.memory) or \
        #         ("Открыть смену" in self.request.call.data):
        #     self.open_day()

        elif self.request.user.memory == "":
            self.submenu()
            # Отобразить пункты меню

    def submenu(self):
        # Формирем сообщение меню приложения.
        from openday.submenu_function import submenu_function
        submenu_function(self)
        return ''

    # def open_day(self):
    #     from openday.open_day_function import open_day_function
    #     return open_day_function(self)





