from cryptographer import Cryptographer
from cli import Argparse
import decorators
from database import DataBase
import Inputvalidation as Validate

def main() -> None:
    Parser = Argparse()
    IOParse = Argparse().CommandValue
    master_key = Argparse().masterkey

    if IOParse['id'] != None:
        Validate.id_validation(IOParse['id'])

    try:
        file = open('pswd.db')
        file.close()
    except FileNotFoundError:
        master_key = input('Enter master key: \n')

        Validate.master_key_validation(master_key)
        Validate.master_key_strenght_validation(master_key)

        Cryptographer.generate_key(master_key)
        print('Master key saved successfully. Please restart the program.')
        exit(0)
    
    if IOParse['args']['password'] != None:
        
    
    Database = DataBase(args=encrypted_args)
    
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