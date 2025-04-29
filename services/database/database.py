import sqlite3

class Database:
    def __init__(self):
        self.__conn = sqlite3.connect('database.db')
        self.__cur = self.__conn.cursor()
    
    def execute(self, sql: str, parametrs: tuple = (1,), commit: bool=False, fetchall: bool=False, fetchone: bool=False):
        if parametrs:
            data = self.__cur.execute(sql, parametrs)
        else:
            data = self.__cur.execute(sql)
        
        if commit:
            self.__conn.commit()
        elif fetchall:
            data.fetchall()
        elif fetchone:
            data.fetchone()
        
        return data