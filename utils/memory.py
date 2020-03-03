from utils.database import Sql
import json

# Пример memory {"app":"openday", "subapp":"Открыть смену", "data":{"name":"Филимонов", .....}}
class Memory(object):
    def __init__(self, user):
        self.user = user
        self.string = self._get()
        if (self.string == "") or (self.string is None):
            self.object = {}
        else:
            self.object = json.loads(self.string)

    def add_app(self, app_name):
        self.object["app"] = app_name
        return self

    def add_subapp(self, subapp_name):
        self.object["subapp"] = subapp_name
        return self

    def add_data(self, **data):
        if "data" not in self.object.keys():
            self.object["data"] = {}
        for key, value in data.items():
            self.object["data"][key] = value
        return self

    def remove(self, param):
        self.object[param] = ""
        return self

    def _get(self):
        query = Sql('snb_auth').select("memory").where("user_id=%s" % self.user.user_id)
        return query.run()[0]["memory"]

    def set(self):
        self.string = self.object
        query = Sql('snb_auth').update(memory=self.string).where("user_id=%s" % self.user.user_id)
        print(query.query)
        query.run()

    def clear(self):
        query = Sql('snb_auth').update(memory="").where("user_id=%s" % self.user.user_id)
        query.run()
        return self


