import sqlite3

class Database:
    def __init__(self):
        self.__conn = sqlite3.connect('database.db')
        self.__cur = self.__conn.cursor()
    
    def execute(self, sql, parametrs, commit, fetchall, fetchone):
        data = self.__cur.execute(sql, parametrs)
        
        if commit:
            self.__conn.commit()
        elif fetchall:
            data.fetchall()
        elif fetchone:
            data.fetchone()
        
        return data