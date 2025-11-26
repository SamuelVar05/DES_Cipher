import hashlib

def derive_des_key(user_key: str) -> bytes:
    # Convertir a bytes y hashear con SHA-256
    digest = hashlib.sha256(user_key.encode('utf-8')).digest()
    
    # Tomar los primeros 8 bytes (64 bits) para DES
    return digest[:8]
