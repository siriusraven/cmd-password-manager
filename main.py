from cryptographer import Cryptographer
from cli import Argparse
from savefilemanager import JsonFileManager
from decorators import TableManager

def main():
    CommandLineInterface = Argparse()
    #provides the account for the save file manager
    SaveFile = JsonFileManager(CommandLineInterface.CommandValue['args']['account_name'])
    #loads the save file
    SaveFile.load_passwords()

if __name__ == '__main__':
    main()