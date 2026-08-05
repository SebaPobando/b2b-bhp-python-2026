# ==========================================
# main_controller.py
# Controlador de ejemplo con rutas GET y POST
# ==========================================
# from flask_app.config.mysqlconnection import connectToMySQL  # Para consultas directas si se necesita

from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.example_model import Usuario

@app.route('/')
def index():
    usuarios = Usuario.get_all()
    return render_template('index.html', usuarios=usuarios)

@app.route('/crear', methods=['POST'])
def crear_usuario():
    data = {
        "nombre": request.form['nombre'],
        "email": request.form['email']
    }
    Usuario.save(data)
    return redirect('/')
