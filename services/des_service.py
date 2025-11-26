from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

class DESService:

    def __init__(self, key: bytes):
        self.key = key

    def encrypt_file(self, input_path, output_path):
        iv = os.urandom(8)
        cipher = DES.new(self.key, DES.MODE_CBC, iv)

        with open(input_path, "rb") as f:
            data = f.read()

        encrypted = cipher.encrypt(pad(data, DES.block_size))

        with open(output_path, "wb") as f:
            f.write(iv + encrypted)

    def decrypt_file(self, input_path, output_path):
        with open(input_path, "rb") as f:
            raw = f.read()

        iv = raw[:8]
        encrypted = raw[8:]

        cipher = DES.new(self.key, DES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(encrypted), DES.block_size)

        with open(output_path, "wb") as f:
            f.write(decrypted)
