from openday.day_class import Day
from utils.memory import Memory
import datetime



def open_day_function(application):
    today = Day(datetime.datetime.now().date())
    user_today = today.for_user(application.request.user)
    memory = Memory(application.request.user)
    try:
        data = memory.object["data"]
    except:
        data = {}
    print("Проверяем открыта ли смена.")
    if user_today.is_close() is True:
        print("Проверяем есть ли имя в ключах даты")
        if "name" not in data.keys():
            memory.add_app("Открытие смены").add_subapp("Открыть смену").add_data(name="").set()
            application.out_text = "Пожалуйста, введите фамилию"

        elif "name" in data.keys():
            print("Имя в ключах есть!")
            if data["name"] == "":
                print("Имя равно пусто")
                name = application.request.message.text
                memory.add_data(name=name).set()
                if user_today.delay_minutes() == 0:
                    print("ИПользователь не опоздал")
                    application.out_text = "Доброе утро!"
                    user_today.open(data["name"], "Ok")
                    # Надо вернуть в меню
                    application.app = "menu"
                    memory.clear()
                else:
                    application.out_text = "Внесите причину задержки на " + str(user_today.delay_minutes()) + " минут."
                    memory.add_data(comment="").set()

            elif data["comment"] == "":
                print("Комментарий пустой записываем его.")
                comment = application.request.message.text
                user_today.open(data["name"], comment)
                application.out_text = "Доброе утро!"
                application.app = "menu"
                memory.clear()
    else:
        application.out_text = "Смена уже открыта"
        application.app = "menu"
    print(today.open_now)
    # application.out_text   # Ответ пользователю в тексте.
    # application.keyboard   # Ответ пользовтелю (Клавиатура)
    # application.memory  Готовый аргумент для дальнейшей работы.
