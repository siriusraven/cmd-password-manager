from cryptographer import Cryptographer
from cli import Argparse
from savefilemanager import JsonFileManager
from decorators import TableManager
from operationmanager import Operations

def main() -> None:
    CommandLineInterface = Argparse()
    IOParse = CommandLineInterface.CommandValue
    #provides the account for the save file manager and the operations manager
    SaveFile = JsonFileManager(IOParse['args']['account_name'])
    #loads the save file
    SaveFile.load_passwords()

    #if the input was to list the passwords it will list  them and exit
    if IOParse['command'] == 'list_passwords':
        pass #list_passwords(SaveFile.passwords)
        exit()

    #if the input was anything other than listing it will put the input into the Operations class and it will deal with it
    Operation = Operations(command=IOParse['command'], args=IOParse['args'], JsonFileManager=SaveFile)

    if Operations != 0:
        SaveFile.passwords.append(Operation)
        print('Password successfully added!')
        exit()
    
    print('Password successfully removed!')

if __name__ == '__main__':
    main()