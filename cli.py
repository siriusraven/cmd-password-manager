import argparse
import sys
# CLI = command line interface
class Argparse:
    def __init__(self) -> None:
        self.CommandValue = None

        commands = [method_name for method_name in dir(object) if callable(getattr(object, method_name))]
        parser = argparse.ArgumentParser(description='A Commandline based password manager.',
                                         usage=f'<masterkey> <command> |<args>| |<args>| ...\nAvailable commands: {commands}')
        parser.add_argument('command', help='Operation to run.')
        parser.add_argument('masterkey')


        self.masterkey = parser.parse_args(sys.argv[1:2])
        args = parser.parse_args(sys.argv[2:3])
        try:
            getattr(self, args.command)()
        except AttributeError:
            print(f'The command "{args.command}" does note exists.')
            exit(22)

    # password id is going to be auto assigned and will not be determined by the user
    def add_password(self) -> None:
        parser = argparse.ArgumentParser(description='Adds new passwords', 
                                         usage='<masterkey> add_password <password name> <password>')
        
        parser.add_argument('name')
        parser.add_argument('password')
        args = parser.parse_args(sys.argv[3:])

        self.CommandValue = {'command': 'add_password',
                             'args': vars(args)}
    
    def remove_password(self) -> None:
        parser = argparse.ArgumentParser(description='Removes passwords', 
                                         usage='<masterkey> remove_password <password-id>')

        parser.add_argument('id')
        args = parser.parse_args(sys.argv[3:])

        self.CommandValue = {'command': 'remove_password',
                                        'args': vars(args)}
    
    # list the passwods inside a table using prettytable
    def list_passwords(self) -> None:
        parser = argparse.ArgumentParser(description='Lists all password', 
                                         usage='<masterkey> list_passwords')
    
        self.CommandValue = {'command': 'list_passwords',
                             'args': None}
        
    def drop_table(self) -> None:
        parser = argparse.ArgumentParser(description='Deletes the table', 
                                         usage='<masterkey> drop_table')
    
        self.CommandValue = {'command': 'drop_table',
                             'args': None}