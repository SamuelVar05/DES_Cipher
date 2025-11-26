import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
ENCRYPT_DIR = os.path.join(UPLOAD_DIR, "encrypted")
DECRYPT_DIR = os.path.join(UPLOAD_DIR, "decrypted")