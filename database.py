import sqlite3
import os

class DataBase:
    def __init__(self, args: dict):
        self.args = args

        try:
            file =open("pswd.db", "x")
            file.close()
        except FileExistsError:
            pass

        connect = sqlite3.connect("pswd.db")
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS passwords(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT)")

        connect.commit()
        connect.close()

    def add_row(self):
        connect = sqlite3.connect("pswd.db")

        connect.execute("INSERT INTO passwords(name, password) VALUES(?, ?)", (self.args['name'], self.args['password']))
        
        connect.commit()
        connect.close()

    def remove_row(self):
        connect = sqlite3.connect("pswd.db")

        connect.execute("DELETE FROM passwords WHERE id = ?", (self.args['id'],))

        connect.commit()
        connect.close()

    def update_row(self):
        connect = sqlite3.connect("pswd.db")

        connect.execute("UPDATE passwords SET name = ?, password = ? WHERE id = ?", (self.args['name'], self.args['password'], self.args['id']))

        connect.commit()
        connect.close()
    
    def list_rows(self):
        connect = sqlite3.connect("pswd.db")

        cursor = connect.cursor()
        cursor.execute("SELECT * FROM passwords")
        rows = cursor.fetchall()

        connect.commit()
        connect.close()
        return rows
    
    @staticmethod
    def drop_table():
        connect = sqlite3.connect("pswd.db")

        connect.execute("DROP TABLE passwords")

        connect.commit()
        connect.close()
        os.remove("pswd.db")

""" DataBase = DataBase(args={"name": "beka", "password": "12433"})
DataBase.drop_table()

print(DataBase.list_rows())

DataBase = DataBase(args={"name": "beka", "password": "12433"})
DataBase.add_row()

print(DataBase.list_rows()) """