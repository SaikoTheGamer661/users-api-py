from flask import Flask, request, jsonify
from database import create_table
from models import create_user, get_user
import bcrypt

app = Flask(__name__)

# crear tabla si no existe
create_table()


@app.route("/")
def home():
    return "API Login funcionando"


# registrar usuario
@app.route("/register", methods=["POST"])
def register():

    data = request.json
    usuario = data["usuario"]
    password = data["password"]

    create_user(usuario, password)

    return jsonify({"message": "Usuario registrado"})


# login usuario
@app.route("/login", methods=["POST"])
def login():

    data = request.json
    usuario = data["usuario"]
    password = data["password"]

    user = get_user(usuario)

    if user:
        stored_password = user[2]  # contraseña encriptada
        # verificar contraseña
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            return jsonify({"message": "Login exitoso"})
    
    return jsonify({"message": "Credenciales incorrectas"}), 401



if __name__ == "__main__":
    app.run(debug=True)