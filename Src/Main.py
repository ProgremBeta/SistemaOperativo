from flask import Blueprint , jsonify, render_template, request, redirect, url_for,session, flash
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

@main.route('/logueado', methods=['POST'])
def logueado():
    nombre = request.form['nombre']

    usuario = Usuarios.query.filter_by(nombre=nombre).first()

    if usuario:
        session['user_id'] = usuario.id
        session['user_name'] = usuario.nombre
        flash(f"Bienvenido, {usuario.nombre}", "success")
        return redirect('/usuariosregistrados')
    else:
        flash("Nombre incorrecto. Por favor, inténtalo de nuevo.", "danger")
        return redirect('/')


@main.route('/registro')
def registro():
    return render_template("Registro.html")

@main.route('/registrando' , methods = ['POST'])
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