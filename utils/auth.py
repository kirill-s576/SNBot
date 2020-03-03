# from . import database
from utils.database import Sql
import settings

# ЕСТЬ БОЛЬШОЙ НЕДОСТАТОК! КЛАСС РАБОТАЕТ ТОЛЬКО С НАПИСАВШИМ ПОЛЬЗОВАТЕЛЕМ, ПЕРЕДАВАЯ message
# Надо наверное созлать отдельный класс, который работает только с пользователем.
# Создавая объект класса USER.

class User(object):
    def __init__(self, **data):
        for key, value in data.items():
            if key == 'message':
                self.message = value
                self.user_id = self.message.chat.id
                self.first_name = self.message.chat.first_name
                self.last_name = self.message.chat.last_name
                self.full_name = self.first_name + " " + self.last_name
                self.user = Sql('snb_auth').select("*").where("user_id=%s" % self.user_id).run()[0]
                self.memory = self.user['memory']
                self.link = self.user['link']
                self.app = self.user['app']
                self.open_time = self.user['open_time']
                if self.user is None:
                    self._new_user()
                    self.user_type = 'not_verificated'
                else:
                    self.user_type = self.user['user_type']

            if key == 'chat_id':
                self.user_id = value
                self.user = Sql('snb_auth').select("*").where("user_id=%s" % self.user_id).run()

    # Функция создания нового пользователя. Инициализируется автоматически при создании объекта класса.
    def _new_user(self):
        self.user_type = 'not_verificated'
        new_user_query = Sql('snb_auth').insert(user_id=self.user_id,
                                                first_name=self.first_name,
                                                last_name=self.last_name,
                                                full_name=self.full_name,
                                                user_type=self.user_type)
        new_user_query.run()
        print("Создан новый пользователь " + self.full_name)




    # Функция изменения типа пользователя
    def set_user_type(self, user_type):
        a = Sql('snb_auth').update(user_type=str(user_type)).where("user_id=%s" % self.user_id)
        a.run()
        print("Пользователю "+self.full_name+" присвоен тип " + user_type)

    def set_app(self, app_name):
        a = Sql('snb_auth').update(app=str(app_name)).where("user_id=%s" % self.user_id)
        a.run()

    def get_user_menu(self):
        if self.user_type == "admin":
            return settings.menu_attr_admin

        elif self.user_type == "user":
            return settings.menu_attr_user

        elif self.user_type == "shop":
            return settings.menu_attr_shop

        elif self.user_type == "not_verificated":
            return settings.menu_attr_not_ver


    def set_link(self, link, current_mid):
        a = Sql('snb_auth').update(link=str(link), current_mid=str(current_mid)).where("user_id=%s" % self.user_id)
        a.run()
        return ''






