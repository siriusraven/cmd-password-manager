from prettytable import PrettyTable

class TableManager:
    def __init__(self, JsonFileManager) -> None:
        self.PasswordTable = PrettyTable()
        self.PasswordTable.field_names = ['name', 'password', 'id']
        self.passswords = JsonFileManager.passwords

        self.PrintTable()
    def PrintTable(self) -> None:
        for password in self.passswords:
            self.PasswordTable.add_row(password['name'], password['password'], password['id'])
        
        self.PasswordTable.sortby = 'id'
        print(self.PasswordTable)
