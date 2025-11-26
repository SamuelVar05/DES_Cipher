import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPDATE_DIR = os.path.join(BASE_DIR, "uploads")
ENCRYPT_DIR = os.path.join(UPDATE_DIR, "encrypted")
DECRYPT_DIR = os.path.join(UPDATE_DIR, "decrypted")