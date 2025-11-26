import os
from config.settings import UPLOAD_DIR, ENCRYPT_DIR, DECRYPT_DIR
from services.des_service import DESService
from services.key_derivation_service import derive_des_key

def handle_encrypt(file, user_key):
    """
    Recibe un archivo y la clave del usuario.
    Guarda el archivo temporalmente, deriva la clave, y lo encripta.
    """
    # Derivar clave DES (8 bytes)
    key = derive_des_key(user_key)
    des_service = DESService(key)

    filename = file.filename
    input_path = os.path.join(UPLOAD_DIR, filename)
    output_path = os.path.join(ENCRYPT_DIR, filename + ".des")

    # Guardar archivo subido
    file.save(input_path)

    # Encriptar
    des_service.encrypt_file(input_path, output_path)

    return output_path


def handle_decrypt(file, user_key):
    """
    Recibe archivo .des + la clave del usuario.
    Deriva clave, desencripta y devuelve ruta de archivo resultante.
    """
    key = derive_des_key(user_key)
    des_service = DESService(key)

    filename = file.filename
    input_path = os.path.join(UPLOAD_DIR, filename)
    output_path = os.path.join(
        DECRYPT_DIR,
        filename.replace(".des", "")  # quitar .des para recuperar nombre original
    )

    # Guardar archivo subido temporalmente
    file.save(input_path)

    # Desencriptar
    des_service.decrypt_file(input_path, output_path)

    return output_path
