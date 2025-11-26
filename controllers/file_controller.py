import os
from services.des_service import DESService

des_service = DESService("Hello")

UPLOAD_DIR = "uploads"
ENCRYPT_DIR = os.path.join(UPLOAD_DIR, "encrypted")
DECRYPT_DIR = os.path.join(UPLOAD_DIR, "decrypted")

def handle_encrypt(file):
    filename = file.filename
    input_path = os.path.join(UPLOAD_DIR, filename)
    output_path = os.path.join(ENCRYPT_DIR, filename + ".des")

    file.save(input_path)
    des_service.encrypt_file(input_path, output_path)

    return output_path

def handle_decrypt(file):
    filename = file.filename
    input_path = os.path.join(UPLOAD_DIR, filename)
    output_path = os.path.join(
        DECRYPT_DIR,
        filename.replace(".des", "")
    )

    file.save(input_path)
    des_service.decrypt_file(input_path, output_path)

    return output_path
