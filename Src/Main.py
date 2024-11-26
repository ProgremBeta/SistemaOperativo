from flask import Blueprint , jsonify, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from Src.Servidor.ConexionDB import Usuarios
from Src.Servidor.BaseDatos import db


main = Blueprint('main', __name__)

mysql = MySQL()

@main.route('/')
def index():
    return render_template("index.html")


@main.route('/login')
def login():
    return render_template("Login.html")

@main.route('/login')
def logueado():
    return "logiado"


@main.route('/registro')
def registro():
    return render_template("Registro.html")

@main.route('/login' , methods = ['POST'])
def Registrando():
    id = request.form['id']
    nombre = request.form['nombre']
    apellido = request.form['apellido']

    NuevoRegistro = Usuarios(id,nombre,apellido)

    db.session.add(NuevoRegistro)
    db.session.commit()

    return redirect('/')


@main.route('/usuariosregistrados')
def usuariosRegistrados():
    usuarios = Usuarios.query.all()
    return render_template("UsuariosRegistrados.html", usuarios=usuarios)