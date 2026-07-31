from flask import render_template, redirect, request, session, bcrypt
from flask_app import app
from flask_app.models.usuario_model import Usuario
from flask_bcrypt import Bcrypt 

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear', methods=['POST'])
def crear_usuario():
    
    pass_hasheado = bcrypt.generate_password_hash(request.form['password'])
    
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": pass_hasheado
    }
    
    nuevo_id = Usuario.save(data) 
    session['usuario_id'] = nuevo_id 
    
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/cerrar_sesion')
def cerrar_sesion():
    return render_template('index.html')