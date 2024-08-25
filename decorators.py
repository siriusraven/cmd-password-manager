from prettytable import PrettyTable

class TableManager:
    def __init__(self) -> None:
        self.PasswordTable = PrettyTable()
        self.PasswordTable.field_names = ['website', 'password']
    def FillTable(self, passwords) -> None:
        self.
