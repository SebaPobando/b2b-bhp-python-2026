from flask_app import app #Importamos la app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import Usuario


@app.route("/")
def index():
    usuarios = Usuario.get_all()
    print(usuarios)
    return render_template("index.html", usuarios=usuarios)

@app.route("/crear", methods=['POST'])
def crear():
    datos = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email']
    }
    Usuario.save(datos)
    return redirect('/')