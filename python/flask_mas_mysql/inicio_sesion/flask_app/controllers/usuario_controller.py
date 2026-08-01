from flask_app import app
from flask_app.models.usuario_model import Usuario
from flask_bcrypt import Bcrypt
from flask import render_template, redirect, request, session, flash

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear', methods=['POST'])
def crear_usuario():
    
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": request.form['password'],
        "validpassword":request.form['validpassword']
    }
    
    # AGREGAR VALIDACIONES
    
    pass_hasheada = bcrypt.generate_password_hash(request.form['password'])

    data['password'] = pass_hasheada
    
    Usuario.save(data)
    
    # GUARDAR ID EN SESIÓN
    
    session["nombre_usuario"] = request.form['nombre']
    
    return redirect('/dashboard')

@app.route("/login", methods=["POST"])
def iniciar_sesion():
    
    usuario = Usuario.buscar_por_email({"email": request.form["email"]})
    
    if not usuario:
        flash("Correo o contraseña incorrectos.", "login")
        return redirect("/")
    
    if not bcrypt.check_password_hash(usuario.password, request.form["password"]):
        
        flash("Correo o contraseña incorrectos.", "login")
        return redirect("/")
    
    session["usuario_id"] = usuario.id
    session["nombre_usuario"] = usuario.nombre
    
    return redirect("/dashboard")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/cerrar_sesion')
def cerrar_sesion():
    session.clear()
    return render_template('index.html')