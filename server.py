from flask import Flask, request, redirect, render_template
from seguridad import cifrar_simetrico, generar_hash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['username']
    contraseña = request.form['password']

    cifrada = cifrar_simetrico(contraseña)
    hash_contra = generar_hash(contraseña)

    print("Usuario:", usuario)
    print("Contraseña cifrada:", cifrada)
    print("Hash:", hash_contra)

    mensaje = "¡Sus datos han sido ingresados y la clave ha sido generada!"
    return render_template("login.html", mensaje=mensaje)

app.run(debug=True)
