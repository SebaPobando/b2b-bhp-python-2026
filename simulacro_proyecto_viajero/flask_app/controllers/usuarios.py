from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.usuario import Usuario
from flask_app.models.viaje import Viaje
import datetime

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    usuarios = Usuario.get_all()
    print(usuarios)
    return render_template('index.html')

@app.route('/registro_ok')
def ok():
    return render_template('ok.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    if not Usuario.validar_registro(request.form):
        return redirect('/')

    contrasena_hash = bcrypt.generate_password_hash(request.form['contrasena'])

    datos = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'contrasena': contrasena_hash,
    }

    Usuario.save(datos)
    return redirect('/registro_ok')

@app.route('/dashboard')
def dashboard():
    print(session)
    if 'usuario_id' not in session:
        print("No hay usuario logeado, no se puede mostrar el dashboard")
        return redirect('/')

    usuario = Usuario.get_by_id({'id': session['usuario_id']})
    viajes = Viaje.get_all_valid_trips()
    print(viajes)

    return render_template('dashboard.html', usuario=usuario, viajes=viajes)

@app.route('/login', methods=['POST'])
def login():
    usuario = Usuario.get_by_email({'email': request.form['email']})
    if not usuario or not bcrypt.check_password_hash(usuario.contrasena, request.form['contrasena']):
        flash("Credenciales no validas, intente de nuevo", "login")
        return redirect('/')

    session['usuario_id'] = usuario.id
    session['usuario_nombre'] = usuario.nombre

    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')