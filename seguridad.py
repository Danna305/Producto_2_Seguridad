from cryptography.fernet import Fernet
import hashlib

# Clave simétrica
clave = Fernet.generate_key()
fernet = Fernet(clave)

def cifrar_simetrico(texto):
    return fernet.encrypt(texto.encode()).decode()

def generar_hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()
