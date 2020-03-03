import pymysql
import pymysql.cursors
import settings

class Sql:

    def __init__(self, table):

        self.table = table
        self.query = ""
        self.connection = None

    def select(self, *data):
        self.query = "SELECT " + ", ".join(data)
        self.query = self.query + " FROM " + self.table
        return self

    def where(self, data):
        self.query = self.query + " WHERE " + str(data)
        return self

    def odrer_by(self, data):
        self.query = self.query + " ORDER BY " + str(data)
        return self

    def odrer_by_desc(self, data):
        self.query = self.query + " ORDER BY " + str(data) + " DESC"
        return self

    def insert(self, **data):
        self.query = "INSERT INTO " + self.table\
                     + " (" + ", ".join(data.keys())+") "\
                     + "VALUES" + " (" + ", ".join("'%s'" % str(i) for i in data.values())+") "

        return self

    def update(self, **data):
        self.query = "UPDATE " + self.table + " SET "
        self.query = self.query + ", ".join((i+"='"+str(data[i]).replace("'", '"')+"'") for i in data.keys())
        return self

    def run(self):
        self.connection = pymysql.connect(host=settings.SQL_HOST,
                                          user=settings.SQL_USER,
                                          password=settings.SQL_PASSWORD,
                                          db=settings.SQL_NAME,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

        cursor = self.connection.cursor()
        cursor.execute(self.query)
        if "SELECT" in self.query:
            commit_result = cursor.fetchall()
            self.connection.close()
            try:
                a = commit_result[0]
                return commit_result
            except Exception as e:
                print(e)
                print(self.query)
                return None
        else:
            self.connection.commit()
            self.connection.close()
            return ''


