import json
import os

class JsonFileManager:
    def __init__(self) -> None:
        self.passwords = []

    # save the passwords inside a json file | strictly uses python dictionaries for saving
    def save_passwords(self) -> None:
        with open('pswd.json', 'w') as file:
            json.dump(self.passwords, file, indent=4)

    # loads the password from the save file | loads it into a list and as dictionaries
    def load_passwords(self) -> None:
        try:
            with open('pswd.json', 'r') as file:
                pass
        except FileNotFoundError:
            self.create_saveFile()

        if os.stat(r'pswd.json').st_size == 0:
            # only runs if the save file is empty >> this will ask for a new master key
            return 0
        with open('pswd.json', 'r') as file:
            self.passwords = json.load(file)

    @staticmethod
    def create_saveFile() -> None:
        try:
            open('pswd.json', 'x')
        except FileExistsError:
            raise Exception(FileExistsError)