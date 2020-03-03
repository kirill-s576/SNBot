import start
class Sender(object):

    def __init__(self, request):
        self.request = request
        self.application = self.request.application

    def send_responce(self):
        text = self.application.out_text
        keyboard = self.application.keyboard
        try:

            start.bot.edit_message_text(text, self.request.message.chat.id, self.request.message.message_id)
            try:
                start.bot.edit_message_reply_markup(self.request.message.chat.id, self.request.message.message_id, reply_markup=keyboard)
            except:
                pass

        except Exception as e:
            print(e)
            try:
                start.bot.send_message(self.request.message.chat.id, text, reply_markup=keyboard)
            except:
                start.bot.send_message(self.request.message.chat.id, text)


    def clear(self):
        chat_id = self.request.message.chat.id
        mid = self.request.message.message_id
        for i in range((mid-10), (mid-1)):
            try:
                start.bot.delete_message(chat_id, mid)
            except:
                pass


