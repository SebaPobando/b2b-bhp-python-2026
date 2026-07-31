from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.usuario_model import Usuario

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear', methods=['POST'])
def crear_usuario():
    data = {
        "nombre": request.form['nombre'],
        "email": request.form['email'],
        "password": request.form['password']
    }
    Usuario.save(data)
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')