import argparse
import sys
# CLI = command line interface
class Argparse:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description='A Commandline based password manager.',
                                         usage=f'<command> |<args>| |<args>| ...\nAvailable commands: {[method_name for method_name in dir(object)
                                                                       if callable(getattr(object, method_name))]}')
        parser.add_argument('command', help='Operation to run.')

        args = parser.parse_args(sys.argv[1:2])
        try:
            getattr(self, args.command)()
        except AttributeError:
            print(f'The command "{args.command}" does note exists.')
            exit()

    # password id is going to be auto assigned and will not be determined by the user
    @staticmethod
    def add_password() -> None:
        parser = argparse.ArgumentParser(description='Adds new keys', 
                                         usage='add_password <password>')

        parser.add_argument('password')
        args = parser.parse_args(sys.argv[2:])
    
    @staticmethod
    def remove_password() -> None:
        parser = argparse.ArgumentParser(description='Adds new keys', 
                                         usage='remove_password <password-id>')

        parser.add_argument('password')
        args = parser.parse_args(sys.argv[2:])
    # list the passwods inside a table using prettytable
    @staticmethod
    def list_passwords() -> None:
        parser = argparse.ArgumentParser(description='Adds new keys', 
                                         usage='list_passwords')

        parser.add_argument('-s', '--sort')
        args = parser.parse_args(sys.argv[2:])