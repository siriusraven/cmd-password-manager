from cryptographer import Cryptographer
from cli import Argparse
import decorators
from database import DataBase

def main() -> None:
    Parser = Argparse()
    IOParse = Argparse().CommandValue

    Database = DataBase(args=IOParse['args'])
    
    if IOParse['command'] == 'list_passwords':
        passwords = Database.list_rows()
        decorators.Table(passwords)
    
    if IOParse['command'] == 'add_password':
        Database.add_row()
    
    if IOParse['command'] == 'remove_password':
        Database.remove_row()

    if IOParse['command'] == 'drop_table':
        Database.drop_table()


if __name__ == '__main__':
    main()