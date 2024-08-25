import json
import os

class jsonFileManager:
    def __init__(self) -> None:
        self.passwords = []
    
    def SavePasswords(self) -> None:
        with open('pswd.json', 'w') as file:
            json.dump(self.passwords, file, indent=4)

    def LoadPasswords(self) -> None:
        try:
            with open('pswd.json', 'r') as file:
                pass
        except FileNotFoundError:
            self.CreateSaveFile()

        if os.stat(r'pswd.json').st_size == 0: 
            print('firstime')
        with open('pswd.json', 'r') as file:
            self.passwords = json.load(file)
    @staticmethod
    def CreateSaveFile() -> None:
        try:
            open('pswd.json', 'x')
        except FileExistsError:
            raise Exception(FileExistsError)

a = jsonFileManager()
a.LoadPasswords()