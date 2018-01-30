import pymysql


class Db(object):
    def __init__(self, **kwargs):
        self.host = kwargs.get('host')
        self.port = kwargs.get('port')
        self.user = kwargs.get('user')
        self.passwd = kwargs.get('passwd')
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd)
        self.cursor = self.conn.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
