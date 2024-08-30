import json
import os

class JsonFileManager:
    def __init__(self, account) -> None:
        self.passwords = []
        self.account = account

    # save the passwords inside a json file | strictly uses python dictionaries for saving
    def save_passwords(self) -> None:
        with open(f'{self.account}.json', 'w') as file:
            json.dump(self.passwords, file, indent=4)

    # loads the password from the save file | loads it into a list and as dictionaries
    def load_passwords(self) -> None:
        try:
            with open(f'{self.account}.json', 'r') as file:
                pass
        except FileNotFoundError:
            self.create_saveFile()

        if os.stat(rf'{self.account}.json').st_size == 0:
            # only runs if the save file is empty >> this will ask for a new master key
            return 0
        with open(f'{self.account}.json', 'r') as file:
            self.passwords = json.load(file)

    def create_saveFile(self) -> None:
        try:
            open(f'{self.account}.json', 'x')
        except FileExistsError:
            raise Exception(FileExistsError)