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

    return redirect('/home')

@app.route('/home')
def home():
    return render_template("home.html")

app.run(debug=True)
