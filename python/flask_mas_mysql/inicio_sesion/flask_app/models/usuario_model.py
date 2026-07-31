from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

class Usuario:
    db = "esquema_sesion"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Guardar un nuevo registro
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    # Obtener todos los registros
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL(cls.db).query_db(query)
        usuarios = []
        for row in results:
            usuarios.append(cls(row))
        return usuarios
    
    @classmethod
    def buscar_por_email(cls, datos):
       query = "SELECT * FROM usuarios WHERE email = %(email)s"
       resultados = connectToMySQL(cls.db).query_db(query, datos)
       if len(resultados) == 1:
           usuario = cls(resultados[0])
           return usuario 
       else:
           return False
       
    @staticmethod
    def validar_form(data):
        patron_letras = re.compile(r'^[^\\W\\d_]+$')
        patron_email = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        valid = True
        if len(data['nombre'])<2 or not patron_letras.match(data['nombre']):
            flash("El nombre debe ser solo letras y tener al menos 2 caracteres.","register-error") 
            valid = False
        if len(data['apellido'])<2 or not patron_letras.match(data['apellido']):
            flash("El apellido debe ser solo letras y tener al menos 2 caracteres.","register-error") 
            valid = False
        if data['password'] != data['validpassword']:
            flash("Las contraseñas deben coincidir.","register-error")
            valid = False
        if not patron_email.match(data['email']):
            flash("El formato de correo no es válido.","register-error")
            valid = False
        if len(data['password'])<8:
            flash("La contraseña debe tener almenos 8 carácteres.","register-error")
            valid = False
        if Usuario.buscar_por_email(data):
            flash("El correo ya se encuentra registrado.","register-error")
            valid = False
        if not bool(re.search(r"\d", data['password'])):
            flash("La contraseña debe tener almenos un número.","register-error")
            valid = False
        if not bool(re.search(r'[A-Z]', data['password'])):
            flash("La contraseña debe tener almenos una mayuscula.","register-error")
            valid = False
        return valid
