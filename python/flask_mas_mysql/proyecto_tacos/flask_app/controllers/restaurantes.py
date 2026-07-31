from flask_app import app  # Importamos la app
from flask import render_template, redirect, request, session, flash
from flask_app.models.restaurante import Restaurante


@app.route('/restaurantes')
def restaurantes():
    # Muestra el formulario para crear restaurantes junto al listado
    restaurantes = Restaurante.get_all()
    return render_template("restaurantes.html", todos_restaurantes=restaurantes)


@app.route('/restaurantes/crear', methods=['POST'])
def crear_restaurante():
    datos = {
        "nombre": request.form['nombre']
    }
    Restaurante.save(datos)
    return redirect('/restaurantes')


@app.route('/restaurantes/mostrar/<int:restaurante_id>')
def detalle_restaurante(restaurante_id):
    datos = {
        'id': restaurante_id
    }
    # Trae el restaurante con la lista de tacos asociados
    restaurante = Restaurante.get_restaurante_y_tacos(datos)
    if not restaurante:
        flash("Ese restaurante no existe")
        return redirect('/restaurantes')
    return render_template("detalle_restaurante.html", restaurante=restaurante)


@app.route('/restaurantes/editar/<int:restaurante_id>')
def editar_restaurante(restaurante_id):
    datos = {
        'id': restaurante_id
    }
    restaurante = Restaurante.get_one(datos)
    if not restaurante:
        flash("Ese restaurante no existe")
        return redirect('/restaurantes')
    return render_template("editar_restaurante.html", restaurante=restaurante)


@app.route('/restaurantes/actualizar/<int:restaurante_id>', methods=['POST'])
def actualizar_restaurante(restaurante_id):
    datos = {
        'id': restaurante_id,
        "nombre": request.form['nombre']
    }
    Restaurante.update(datos)
    return redirect(f"/restaurantes/mostrar/{restaurante_id}")


@app.route('/restaurantes/borrar/<int:restaurante_id>')
def borrar_restaurante(restaurante_id):
    datos = {
        'id': restaurante_id
    }
    Restaurante.delete(datos)
    return redirect('/restaurantes')
