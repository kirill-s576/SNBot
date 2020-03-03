from flask import Flask, request, render_template
import flask
import telebot
import main_router

app = Flask(__name__)

BOT_TOKEN = "900913712:AAHMKGi4AIoURpqii41t11gFHy766QGpBW0"
bot = telebot.TeleBot(BOT_TOKEN)

WEBHOOK_HOST = 'https://213.226.124.119'
WEBHOOK_PORT = 88
WEBHOOK_URL = "%s:%s/%s/" % (WEBHOOK_HOST, WEBHOOK_PORT, BOT_TOKEN)


# Empty webserver index, return nothing, just http 200
@app.route('/')
def index():
    return '<h1>Тестовая страница</h1>'

@app.route('/test')
def index2():
    return render_template('openday.html')

# Process webhook calls
@app.route("/"+BOT_TOKEN+"/", methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


# ОБРАБОТЧИК ТЕКСТОВОГО СООБШЕНИЯ
@bot.message_handler(func=lambda message: True, content_types=['text'])
def regular_message(message):
    main_router.main_router(message)

# ОБРАБОТЧИК ИНЛАЙН НАЖАТИЙ КНОПКИ
@bot.callback_query_handler(func=lambda call: True)
def inline_message(call):
    main_router.main_router(call)

# Remove webhook, it fails sometimes the set if there is a previous webhook
# bot.remove_webhook()


# Set webhook
# bot.set_webhook(url=WEBHOOK_URL,
#                 certificate=open('/python_app/tgbot/cert.pem', 'r'))

if __name__ == '__main__':
    app.run(
        host='213.226.124.119',
        port=WEBHOOK_PORT,
        ssl_context=('/python_projects/sntelebot_v2/cert.pem', '/python_projects/sntelebot_v2/key.pem'),
        debug=True)



