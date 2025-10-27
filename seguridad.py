from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import hashlib

# ===== CIFRADO SIMÉTRICO =====
# Clave simétrica (se genera una vez al iniciar el servidor)
clave = Fernet.generate_key()
fernet = Fernet(clave)

def cifrar_simetrico(texto):
    """Cifra un texto usando AES (Fernet)"""
    return fernet.encrypt(texto.encode()).decode()

def descifrar_simetrico(texto_cifrado):
    """Descifra un texto cifrado simétricamente"""
    return fernet.decrypt(texto_cifrado.encode()).decode()


# ===== CIFRADO ASIMÉTRICO (RSA) =====
# Generar par de claves RSA (pública y privada)
clave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
clave_publica = clave_privada.public_key()

def cifrar_asimetrico(texto):
    """Cifra un texto usando la clave pública RSA"""
    mensaje_bytes = texto.encode()
    texto_cifrado = clave_publica.encrypt(
        mensaje_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Convertir a hexadecimal para facilitar visualización
    return texto_cifrado.hex()

def descifrar_asimetrico(texto_cifrado_hex):
    """Descifra un texto usando la clave privada RSA"""
    texto_cifrado = bytes.fromhex(texto_cifrado_hex)
    mensaje_bytes = clave_privada.decrypt(
        texto_cifrado,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return mensaje_bytes.decode()


# ===== HASH =====
def generar_hash(texto):
    """Genera un hash SHA-256 del texto"""
    return hashlib.sha256(texto.encode()).hexdigest()
