#manages operations
class Operations:
    def __init__(self, command, args, JsonFileManager) -> None:
        self.command = command
        self.args = args
        self.JsonFileManager = JsonFileManager

        getattr(self, command)
    
    def add_password(self) -> dict:
        name = self.args['name']
        password = self.args['password']

        return {'name': name,
                'password': password,
                'id': self.Id_generator()}

    def remove_password(self) -> None:
        Id = self.args['password_id']

        for password in self.JsonFileManager.passwords:
            if password['id'] == Id:
                self.JsonFileManager.passwords.remove(password)
    
    def Id_generator(self) -> int:
        Id = None
        
        return Id