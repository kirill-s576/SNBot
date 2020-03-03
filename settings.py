# Настойки базы данных Sql
SQL_HOST = 'localhost'
SQL_USER = 'root'
SQL_PASSWORD = 'SnDf7rE8'
SQL_NAME = 'telegram_bot_v2'

apps = [
    "Actions",
    "News",
    "TimeManage",
    "ChangeUser"
]

"""Типы пользователей
admin
moder
user
shop
not_verificated - только зарегистрировался и еще не авторизовали
"""

available_apps = [
    "openday",
    "actions"
]

menu_attr_admin = {"main": {
                            "openday": None,
                            "actions": None,
                            "news": None,
                            "contol": None,
                            "delay": None
                            }
                    }

menu_attr_user = {
    "openday": {"*"},
    "actions": {"*"},
    "news": {"*"}
}

menu_attr_shop = {"main": {
                            "openday": None,
                            "actions": None,
                            "news": None,
                            "contol": None,
                            "delay": None
                            }
                    }


menu_translater = {
    "openday": "Открытие смены",
    "actions": "Акции",
    "news": "Новости",
}


menu_attr_not_ver = {
    "main": {
            "actions": None
            }
    }


"""Паттерны
menu - паттерн меню
app: appname паттерн приложения app: название приложения
"""

"""Роутер должен дальще отдавать 
message_id, message_text, message"""

"""{'content_type': 'text', 'message_id': 41, 'from_user': {'id': 356080087, 'is_bot': False, 'first_name': 'Кирилл', 
'username': 's_kirill_91', 'last_name': 'С', 'language_code': 'ru'}, 'date': 1568306550, 'chat': {'type': 'private', 
'last_name': 'С', 'first_name': 'Кирилл', 'username': 's_kirill_91', 'id': 356080087, 'title': None, 
'all_members_are_administrators': None, 'photo': None, 'description': None, 'invite_link': None, 'pinned_message': None,
 'sticker_set_name': None, 'can_set_sticker_set': None}, 'forward_from_chat': None, 'forward_from': None, 'forward_date': None, 
 'reply_to_message': None, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': 'sdfsdf', 
 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 
 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 
 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None,
  'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 
  'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 
  'successful_payment': None, 'connected_website': None, 'json': {'message_id': 41, 'from': {'id': 356080087, 
  'is_bot': False, 'first_name': 'Кирилл', 'last_name': 'С', 'username': 's_kirill_91', 'language_code': 'ru'}, 
  'chat': {'id': 356080087, 'first_name': 'Кирилл','last_name': 'С', 'username': 's_kirill_91', 'type': 'private'}, 
  'date': 1568306550, 'text': 'sdfsdf'}}
"""
