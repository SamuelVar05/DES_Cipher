from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

class DESService:

    def __init__(self, key: bytes):
        self.key = key

    def encrypt_file(self, input_path: str, output_path: str):
        iv = os.urandom(8)
        cipher = DES.new(self.key, DES.MODE_CBC, iv)

        with open(input_path, "rb") as f:
            data = f.read()

        padded = pad(data, DES.block_size)
        encrypted = cipher.encrypt(padded)

        # Guardar IV + encrypted juntos
        with open(output_path, "wb") as f:
            f.write(iv + encrypted)

        return iv

    def decrypt_file(self, input_path: str, output_path: str):
        with open(input_path, "rb") as f:
            content = f.read()

        iv = content[:8]
        encrypted = content[8:]

        cipher = DES.new(self.key, DES.MODE_CBC, iv)
        decrypted_padded = cipher.decrypt(encrypted)
        decrypted = unpad(decrypted_padded, DES.block_size)

        with open(output_path, "wb") as f:
            f.write(decrypted)
