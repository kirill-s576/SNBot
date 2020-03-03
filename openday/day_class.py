from utils.database import Sql
from utils.memory import Memory
import datetime


class Day(object):
    def __init__(self, date):
        self.date = date
        self.open_now = Sql('snb_opentime').select('*').where("DATE(datetime_open)='%s'" % self.date).run()
        self.user = None

    # Добавляем пользователя при необходимости.
    def for_user(self, user):
        self.user = user
        return self

    def status(self):
        # Return open or close
        pass

    # Вносим данные открытия смены с заданными параметрами.
    def open(self, worker_name, comment):
        if self.user is None:
            print("Не задан пользователь. Используйте метод for_user")
        else:
            query = Sql('snb_opentime').insert(user_id=self.user.user_id, datetime_open=datetime.datetime.now(),
                                               last_name=worker_name, comment=comment)
            query.run()

    def close(self):
        pass

    def delay_minutes(self):
        if self.user is None:
            print("Не задан пользователь. Используйте метод for_user")
        else:
            need_time = self.user.open_time   # 10:00:00
            need_datetime = datetime.datetime.combine(datetime.datetime.today(), datetime.datetime.strptime(str(need_time), "%H:%M:%S").time())
            current_time = datetime.datetime.now()
            print(need_datetime)
            print(current_time)
            delta = need_datetime - current_time
            if delta.days < 0:
                # Опоздал
                return int((current_time - need_datetime).seconds/60)
            else:
                # Не опоздал
                return 0


    def is_close(self):
        all_users = self.get_all_users()

        open_users_ids = []
        try:
            for open_user in self.open_now:
                open_users_ids.append(open_user["user_id"])
        except:
            pass

        if self.user is None:
            # Return close users
            close_users_list = []
            for user in all_users:
                if user["user_id"] not in open_users_ids:
                    close_users_list.append(user)
            return close_users_list
        else:
            # Return True or False
            if self.user.user_id not in open_users_ids:
                return True
            else:
                return False

    def get_all_users(self):
        all_users = Sql('snb_auth').select("*").run()
        return all_users



