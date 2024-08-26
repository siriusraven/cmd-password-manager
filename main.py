from cryptographer import Cryptographer
from cli import Argparse
from savefilemanager import JsonFileManager
from decorators import TableManager

def main():
    SaveFile = JsonFileManager()
    SaveFile.load_passwords()
    CommandLineInterface = Argparse()

if __name__ == '__main__':
    main()