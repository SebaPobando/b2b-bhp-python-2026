from flask_app import app  # Importamos la app
from flask import render_template, redirect, request, session, flash
from flask_app.models.complemento import Complemento


@app.route('/complementos')
def complementos():
    # Muestra el formulario para crear complementos junto al listado
    complementos = Complemento.get_all()
    return render_template("complementos.html", todos_complementos=complementos)


@app.route('/complementos/crear', methods=['POST'])
def crear_complemento():
    datos = {
        "nombre_complemento": request.form['nombre_complemento']
    }
    Complemento.save(datos)
    return redirect('/complementos')


@app.route('/complementos/mostrar/<int:complemento_id>')
def detalle_complemento(complemento_id):
    datos = {
        'id': complemento_id
    }
    # Trae el complemento con la lista de tacos en los que aparece
    complemento = Complemento.get_complementos_y_tacos(datos)
    if not complemento:
        flash("Ese complemento no existe")
        return redirect('/complementos')
    return render_template("detalle_complemento.html", complemento=complemento)


@app.route('/complementos/agregar/<int:taco_id>', methods=['POST'])
def agregar_complemento(taco_id):
    # Relación muchos a muchos: asociamos un complemento a un taco
    datos = {
        'taco_id': taco_id,
        'complemento_id': request.form['complemento_id']
    }
    Complemento.agregar_a_taco(datos)
    return redirect(f"/mostrar/{taco_id}")


@app.route('/complementos/quitar/<int:taco_id>/<int:complemento_id>')
def quitar_complemento(taco_id, complemento_id):
    datos = {
        'taco_id': taco_id,
        'complemento_id': complemento_id
    }
    Complemento.quitar_de_taco(datos)
    return redirect(f"/mostrar/{taco_id}")


@app.route('/complementos/borrar/<int:complemento_id>')
def borrar_complemento(complemento_id):
    datos = {
        'id': complemento_id
    }
    Complemento.delete(datos)
    return redirect('/complementos')
