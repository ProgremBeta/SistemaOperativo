from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from Src.Servidor.ConexionDB import Usuarios
from Src.Servidor.BaseDatos import db

main = Blueprint('main', __name__)

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


@main.route('/registrando', methods=['POST'])
def Registrando():
    id = request.form['id']
    nombre = request.form['nombre']
    apellido = request.form['apellido']

    NuevoRegistro = Usuarios(id, nombre, apellido)

    db.session.add(NuevoRegistro)
    db.session.commit()

    return redirect('/')


@main.route('/usuariosregistrados')
def usuariosRegistrados():
    usuarios = Usuarios.query.all()
    return render_template("UsuariosRegistrados.html", usuarios=usuarios)


@main.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_usuario(id):
    usuario = Usuarios.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        flash("Usuario eliminado exitosamente", "success")
    else:
        flash("Usuario no encontrado", "danger")
    return redirect('/usuariosregistrados')


@main.route('/modificar/<int:id>', methods=['GET', 'POST'])
def modificar_usuario(id):
    usuario = Usuarios.query.get(id)
    if not usuario:
        flash("Usuario no encontrado", "danger")
        return redirect('/usuariosregistrados')

    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.apellido = request.form['apellido']
        db.session.commit()
        flash("Usuario modificado exitosamente", "success")
        return redirect('/usuariosregistrados')

    return render_template("ModificarUsuario.html", usuario=usuario)
