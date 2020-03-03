
# def open(message, data):
#     print("Смена открывается")
#     user_id = message.chat.id
#     query = database.Sql('snb_opentime').select('*').where("user_id='%s' AND DATE(datetime_open)='%s'" % (user_id, datetime.datetime.now().date()))
#     print(query.query)
#     day = query.run()
#     print(str(day))
#     if day is None:
#         last_name = ''
#         comment = ''
#     else:
#         last_name = day['last_name']
#         comment = day['comment']
#
#     if day is None or last_name == '':
#         bot.send_message(user_id, "Введите вашу фамилию:")
#         query = database.Sql('snb_opentime').insert(user_id=user_id, datetime_open=datetime.datetime.now(), last_name="wait")
#         query.run()
#     elif str(last_name) == 'wait':
#         # Проверяем опоздал или нет.
#         query = database.Sql('snb_auth').select('*').where("user_id='%s'" % user_id)
#         user = query.run()
#         need_time = user['open_time']
#         need_datetime = datetime.datetime.combine(datetime.datetime.today(), datetime.datetime.strptime(str(need_time), "%H:%M:%S").time())
#         current_time = datetime.datetime.now()
#         delta = need_datetime - current_time
#         if delta.days < 0:
#             bot.send_message(user_id, "Внесите причину задержки:")
#             query = database.Sql('snb_opentime').update(last_name=str(data), comment="wait").where(
#                 "user_id='%s' AND DATE(datetime_open)='%s'" % (user_id, datetime.datetime.now().date()))
#             query.run()
#         else:
#             bot.send_message(user_id, "Доброе утро!")
#             query = database.Sql('snb_opentime').update(last_name=str(data), comment="Ok").where(
#                 "user_id='%s' AND DATE(datetime_open)='%s'" % (user_id, datetime.datetime.now().date()))
#             query.run()
#             menu_by_link(message, "menu/")
#     elif comment == 'wait':
#         query = database.Sql('snb_opentime').update(comment=str(data)).where(
#             "user_id='%s' AND DATE(datetime_open)='%s'" % (user_id, datetime.datetime.now().date()))
#         query.run()
#         bot.send_message(user_id, "Доброе утро!")
#         menu_by_link(message, "menu/", new=True)
#     else:
#         bot.send_message(user_id, "Смена уже открыта!")