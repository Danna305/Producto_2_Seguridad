from flask import Flask, request, render_template_string
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import hashlib

app = Flask(__name__)

# 🔐 Simétrico: clave y objeto Fernet
symmetric_key = Fernet.generate_key()
cipher = Fernet(symmetric_key)

# 🔑 Asimétrico: claves pública y privada
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# 🧾 HTML del login
login_html = """
<form method="post">
    <h1>Inicio de sesión</h1>
    <label>Usuario:</label><input type="text" name="username" required><br>
    <label>Contraseña:</label><input type="password" name="password" required><br>
    <input type="submit" value="Iniciar sesión">
</form>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # 🧮 Hash de la contraseña
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # 🔐 Cifrado simétrico del usuario
        encrypted_user = cipher.encrypt(username.encode())

        # 🔑 Cifrado asimétrico de la contraseña
        encrypted_pass = public_key.encrypt(
            password.encode(),
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )

        return f"""
        <h2>Datos procesados:</h2>
        <p>Usuario cifrado (simétrico): {encrypted_user}</p>
        <p>Contraseña cifrada (asimétrico): {encrypted_pass}</p>
        <p>Contraseña hash (SHA-256): {hashed_password}</p>
        """
    return render_template_string(login_html)

if __name__ == "__main__":
    app.run(debug=True)
