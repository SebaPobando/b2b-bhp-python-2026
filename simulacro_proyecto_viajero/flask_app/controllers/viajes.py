from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.usuario import Usuario
from flask_app.models.viaje import Viaje
import datetime

@app.route('/nuevo')
def nuevo():
    return render_template('nuevo.html')

@app.route('/viajes/crear', methods=['POST'])
def crear():
    datos = {
        'destino': request.form['destino'],
        'fecha_inicio': request.form['fecha_inicio'],
        'fecha_fin': request.form['fecha_fin'],
        'itinerario': request.form['itinerario'],
        'organizador_id': session['usuario_id']
    }
    Viaje.save(datos)
    return redirect('/dashboard')