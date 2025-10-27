from flask import Flask, request, redirect, render_template
from seguridad import cifrar_simetrico, cifrar_asimetrico, generar_hash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['username']
    contraseña = request.form['password']

    # Aplicar los 3 tipos de algoritmos requeridos
    cifrada_simetrica = cifrar_simetrico(contraseña)
    cifrada_asimetrica = cifrar_asimetrico(contraseña)
    hash_contra = generar_hash(contraseña)

    # Mostrar resultados en consola
    print("\n" + "="*60)
    print("RESULTADOS DE SEGURIDAD")
    print("="*60)
    print(f"Usuario: {usuario}")
    print(f"\n1. CIFRADO SIMÉTRICO (AES/Fernet):")
    print(f"   {cifrada_simetrica}")
    print(f"\n2. CIFRADO ASIMÉTRICO (RSA-2048):")
    print(f"   {cifrada_asimetrica}")
    print(f"\n3. HASH (SHA-256):")
    print(f"   {hash_contra}")
    print("="*60 + "\n")

    mensaje = "¡Datos procesados correctamente! Revisa la consola para ver los resultados de cifrado."
    return render_template("login.html",
                         mensaje=mensaje,
                         usuario=usuario,
                         cifrado_simetrico=cifrada_simetrica,
                         cifrado_asimetrico=cifrada_asimetrica[:80] + "...",  # Mostrar solo parte
                         hash_generado=hash_contra)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
