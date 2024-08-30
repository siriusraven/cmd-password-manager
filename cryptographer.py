from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import hashlib
import os

# encrypts / decrypts the json file
class Cryptographer:
    @staticmethod
    def generate_key(master_password: str) -> bytes:
        salt = os.urandom(16)
        hash_value = hashlib.pbkdf2_hmac('sha256', master_password.encode(), salt, 100000)

        #out:
        salted_hash_hex = hash_value.hex()
        salt_hex = salt.hex()
        with open("key.env", "w") as f:
            f.write(f"AES_KEY={salted_hash_hex}\nSALT={salt_hex}")

    @staticmethod
    def derive_key(master_password: str, salt: bytes, iterations: int = 100000) -> bytes:
        # Derive a 32-byte key from the master password using PBKDF2
        key = PBKDF2(master_password, salt, dkLen=32, count=iterations)
        return key

    @staticmethod
    def encrypt_password(password: str, key: bytes) -> bytes:
        iv = os.urandom(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_password = pad(password.encode(), AES.block_size)
        encrypted_password = iv + cipher.encrypt(padded_password)
        return encrypted_password

    @staticmethod
    def decrypt_password(encrypted_password: bytes, key: bytes) -> str:
        iv = encrypted_password[:16]
        encrypted_message = encrypted_password[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_password = cipher.decrypt(encrypted_message)
        password = unpad(padded_password, AES.block_size)
        return password.decode()    
    
    @staticmethod
    def verify_master_password(master_password: str, salt: bytes, stored_hash: bytes) -> bool:
        derived_hash = hashlib.pbkdf2_hmac('sha256', master_password.encode(), salt, 100000)
        return derived_hash == stored_hash

    
#Cryptographer.generate_key("0k0$_B3k4")