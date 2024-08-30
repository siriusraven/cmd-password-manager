from prettytable import PrettyTable

def Table(rows: list) -> None:
    PasswordTable = PrettyTable()
    PasswordTable.field_names = ['id', 'name', 'password']

    PasswordTable.add_rows(rows)
    PasswordTable.sortby = 'id'
    print(PasswordTable)
    