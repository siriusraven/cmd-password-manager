import argparse
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

data = b"babababa"
passwd = "secret"

# encrypts / decrypts the json file
class Cryptographer:
    @staticmethod
    def generate_key(password: str, key_size: int = 32) -> bytes:
        password_bytes = password.encode('utf-8')
        salt = get_random_bytes(16)
        key = PBKDF2(password_bytes, salt, dkLen=key_size, count=1)
        return key, salt

    @staticmethod
    def encryption(data: bytes, key: bytes):
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = pad(data, AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)
        return iv + encrypted_data

    @staticmethod
    def decryption(encdata: bytes, key: bytes):
        iv = encdata[:AES.block_size]
        encrypted_data = encdata[AES.block_size:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_padded_data = cipher.decrypt(encrypted_data)
        unpadded_data = unpad(decrypted_padded_data, AES.block_size)
        return unpadded_data

    """ key, salt = generate_key(passwd)
    encrypted_data = encryption(data, key)
    print("Encrypted:", encrypted_data)
    decrypted_data = decryption(encrypted_data, key)
    print("Decrypted:", decrypted_data.decode('utf-8')) """



# command line interface
class Argparse:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description='A Commandline based password manager.',
                                         help='<command> |<args>| |<args>| ...', 
                                         usage=f'Available commands: {[method_name for method_name in dir(object)
                                                                       if callable(getattr(object, method_name))]}')
        parser.add_argument('command', help='Operation to run.')

        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print(f'Error: Command "{args.command}" is not defined')
            parser.print_help()
        getattr(self, args.command)()
        
    # password id is going to be auto assigned and will not be determined by the user
    @staticmethod
    def add_password() -> None:
        parser = argparse.ArgumentParser(description='Adds new keys', 
                                         help='add_password <password>')

        parser.add_argument('password')
        args = parser.parse_args(sys.argv[2:])
    
    @staticmethod
    def remove_password() -> None:
        parser = argparse.ArgumentParser(description='Adds new keys', 
                                         help='remove_password <password-id>')

        parser.add_argument('password')
        args = parser.parse_args(sys.argv[2:])
    # list the passwods inside a table using prettytable
    @staticmethod
    def list_passwords() -> None:
        parser = argparse.ArgumentParser(description='Adds new keys', 
                                         help='list_passwords')

        parser.add_argument('-s', '--sort')
        args = parser.parse_args(sys.argv[2:])