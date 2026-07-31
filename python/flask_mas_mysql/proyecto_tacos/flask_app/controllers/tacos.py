from flask_app import app #Importamos la app
from flask import render_template,redirect,request,session,flash
from flask_app.models.taco import Taco
from flask_app.models.restaurante import Restaurante
from flask_app.models.complemento import Complemento

@app.route('/')
def index():
    # El formulario necesita la lista de restaurantes para armar el select
    restaurantes = Restaurante.get_all()
    return render_template("index.html", todos_restaurantes = restaurantes)

@app.route('/crear',methods=['POST'])
def crear():
    datos = {
        "tortilla":request.form['tortilla'],
        "guiso": request.form['guiso'],
        "salsa": request.form['salsa'],
        "restaurante_id": request.form['restaurante_id'],
    }
    Taco.save(datos)
    return redirect('/tacos')

@app.route('/tacos')
def tacos():
    tacos = Taco.get_all()
    return render_template("resultados.html",todos_tacos = tacos)

@app.route('/mostrar/<int:taco_id>')
def detalle(taco_id):
    datos = {
        'id': taco_id
    }
    # Traemos el taco con sus complementos y la lista completa para el select
    taco = Taco.get_taco_con_complementos(datos)
    if not taco:
        flash("Ese taco no existe")
        return redirect('/tacos')
    return render_template("detalle.html", taco = taco, todos_complementos = Complemento.get_all())

@app.route('/editar/<int:taco_id>')
def editar(taco_id):
    datos = {
        'id': taco_id
    }
    taco = Taco.get_one(datos)
    if not taco:
        flash("Ese taco no existe")
        return redirect('/tacos')
    return render_template("editar.html", taco = taco, todos_restaurantes = Restaurante.get_all())

@app.route('/actualizar/<int:taco_id>', methods=['POST'])
def actualizar(taco_id):
    datos = {
        'id': taco_id,
        "tortilla":request.form['tortilla'],
        "guiso": request.form['guiso'],
        "salsa": request.form['salsa'],
        "restaurante_id": request.form['restaurante_id'],
    }
    Taco.update(datos)
    return redirect(f"/mostrar/{taco_id}")

@app.route('/borrar/<int:taco_id>')
def borrar(taco_id):
    datos = {
        'id': taco_id,
    }
    Taco.delete(datos)
    return redirect('/tacos')
