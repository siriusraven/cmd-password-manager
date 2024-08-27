from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

# encrypts / decrypts the json file
class Cryptographer:
    @staticmethod
    def generate_key(password: str, key_size: int = 32) -> bytes:
        password_bytes = password.encode('utf-8')
        salt = get_random_bytes(16)
        key = PBKDF2(password_bytes, salt, dkLen=key_size, count=1)
        return key, salt

    @staticmethod
    def encryption(data: bytes, key: bytes) -> bytes:
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = pad(data, AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)
        return iv + encrypted_data

    @staticmethod
    def decryption(encdata: bytes, key: bytes) -> bytes:
        iv = encdata[:AES.block_size]
        encrypted_data = encdata[AES.block_size:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_padded_data = cipher.decrypt(encrypted_data)
        unpadded_data = unpad(decrypted_padded_data, AES.block_size)
        return unpadded_data