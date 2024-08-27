#manages operations
class Operations:
    def __init__(self, command, args) -> None:
        self.command = command
        self.args = args

        getattr(self, command)
    
    def add_password(self, Id) -> None:
        name = self.args['name']
        password = self.args['password']

        return {'name': name, 
                'password': password,
                'id': Id}

    def remove_password(self) -> None:
        return 0
    
    def Id_generator(self) -> int:
        Id = None

        return Id