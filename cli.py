import argparse
import sys
# CLI = command line interface
class Argparse:
    def __init__(self) -> None:
        self.CommandValue = None

        commands = [method_name for method_name in dir(object) if callable(getattr(object, method_name))]
        parser = argparse.ArgumentParser(description='A Commandline based password manager.',
                                         usage=f'<command> |<args>| |<args>| ...\nAvailable commands: {commands}')
        parser.add_argument('command', help='Operation to run.')

        args = parser.parse_args(sys.argv[1:2])
        try:
            getattr(self, args.command)()
        except AttributeError:
            print(f'The command "{args.command}" does note exists.')
            exit(22)

    # password id is going to be auto assigned and will not be determined by the user
    def add_password(self) -> None:
        parser = argparse.ArgumentParser(description='Adds new passwords', 
                                         usage='add_password <password name> <password>')
        
        parser.add_argument('name')
        parser.add_argument('password')
        args = parser.parse_args(sys.argv[2:])

        self.CommandValue = {'command': 'add_password',
                             'args': vars(args)}
    
    def remove_password(self) -> None:
        parser = argparse.ArgumentParser(description='Removes passwords', 
                                         usage='remove_password <password-id>')

        parser.add_argument('id')
        args = parser.parse_args(sys.argv[2:])

        self.CommandValue = {'command': 'remove_password',
                                        'args': vars(args)}
    
    # list the passwods inside a table using prettytable
    def list_passwords(self) -> None:
        parser = argparse.ArgumentParser(description='Lists all password', 
                                         usage='list_passwords')
    

        self.CommandValue = {'command': 'list_passwords',
                             'args': None}
        
    def drop_table(self) -> None:
        parser = argparse.ArgumentParser(description='Deletes the savefile', 
                                         usage='drop_table')
    

        self.CommandValue = {'command': 'drop_table',
                             'args': None}