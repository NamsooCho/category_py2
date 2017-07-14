# -*- coding: utf-8 -*-

import psycopg2
 
class Dao(object):
    def __init__(self):
        self.conn = psycopg2.connect("host='localhost' dbname='catego' user='catego' password='catego'")

    def Close(self):
        self.conn.close()

    def GetAllData(self):
        cur = self.conn.cursor()
        cur.execute("SELECT after, category FROM news where type = 1 order by idx;")
        rows = cur.fetchall()
        cur.close()
        return rows

    def GetAllDataDev(self):
        cur = self.conn.cursor()
        cur.execute("SELECT after, category FROM news where type = 2 order by idx;")
        rows = cur.fetchall()
        cur.close()
        return rows

    def GetBeforeText(self):
        cur = self.conn.cursor()
        cur.execute("SELECT before, idx FROM news where proc = false or proc is null;")
        rows = cur.fetchall()
        cur.close()
        return rows

    def SaveAfterProcessing(self, after, idx):
        cur = self.conn.cursor()
        cur.execute("UPDATE news SET after = %s, proc = true where idx = %s;", (after, idx))
        self.conn.commit()
        cur.close()
