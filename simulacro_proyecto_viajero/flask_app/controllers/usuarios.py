from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.usuario import Usuario

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

    datos = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'contrasena': request.form['contrasena'],
    }
    Usuario.save(datos)
    return redirect('/registro_ok')

