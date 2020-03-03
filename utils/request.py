from utils.auth import User  # Класс пользователя

# В обязательном порядке прописать импорт новых приложений
import menu
from menu.application import Application

import openday
from openday.application import Application

import actions
from actions.application import Application



from utils.sender import Sender

class Request(object):
    def __init__(self, call_or_message):

        try:
            # Это коллбэк сообщение
            self.message = call_or_message.message
            self.call = call_or_message
        except Exception as e:
            print(e)
            # Это обычное сообщение
            self.message = call_or_message
            self.call = None

        self.user = User(message=self.message)

        # Инициализируем приложение
        self.application = eval(str(self.user.app) + '.application.Application(self)')

        # Инициализируем приложение и получаем от него данные.
        self.application.out_result()

        # Проверяем ответ на случай, если нужно совершить действия не требующие выдачу пользователю.
        self.check_responce()



    def check_responce(self):
        try:
            self.send_result()
        except Exception as e:
            print(e)
        # Если надо поменять приложение.
        if self.application.app != str(self.user.app):
            # Меняем в базе имя приложения, с которым работает пользователь.
            self.user.set_app(self.application.app)
            # Инициализируем приложение
            self.application = eval(str(self.application.app) + '.application.Application(self)')
            # Инициализируем приложение и получаем от него данные.
            self.application.out_result()
            # Отправляем результат!
            self.send_result()

    def send_result(self):
        sender = Sender(self)
        sender.send_responce()
        return self





