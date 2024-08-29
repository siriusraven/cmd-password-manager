import argparse
import sys
# CLI = command line interface
class Argparse:
    def __init__(self) -> None:
        self.CommandValue = None

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
    def add_password(self) -> None:
        parser = argparse.ArgumentParser(description='Adds new keys', 
                                         usage='add_password <website / app name> <password> <account>')
        
        parser.add_argument('name')
        parser.add_argument('password')
        parser.add_argument('account_name')
        args = parser.parse_args(sys.argv[2:])

        self.CommandValue = {'command': 'add_password',
                             'args': vars(args)}
    
    def remove_password(self) -> None:
        parser = argparse.ArgumentParser(description='Adds new keys', 
                                         usage='remove_password <password-id> <account>')

        parser.add_argument('account_name')
        parser.add_argument('password_id')
        args = parser.parse_args(sys.argv[2:])

        self.CommandValue = {'command': 'remove_password',
                                        'args': vars(args)}
    
    # list the passwods inside a table using prettytable
    def list_passwords(self) -> None:
        parser = argparse.ArgumentParser(description='Adds new keys', 
                                         usage='list_passwords <account_name> -s |<name>| |<id>| |<password>|')
        
        parser.add_argument('account_name')
        parser.add_argument('-s', '--sort')
        args = parser.parse_args(sys.argv[2:])

        self.CommandValue = {'command': 'list_passwords',
                             'args': vars(args)}