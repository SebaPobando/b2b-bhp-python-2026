from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.contrasena = data['contrasena']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """INSERT INTO usuarios (nombre, apellido, email, contrasena)
                   VALUES (%(nombre)s,%(apellido)s,%(email)s,%(contrasena)s);"""

        return connectToMySQL('esquema_viajero_frecuente').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        # resultados = connectToMySQL('esquema_usuarios').query_db(query)
        resultados = connectToMySQL('esquema_viajero_frecuente').query_db(query)

        usuarios = []

        for usuario in resultados:
            usuarios.append(cls(usuario))

        return usuarios

    @staticmethod
    def validar_registro(usuario):
        es_valido = True
        if(len(usuario['nombre'].strip())) < 2:
            flash("El nombre debe tener al menos 2 caracteres para registrarse", "registro")
            es_valido = False
        if(len(usuario['apellido'].strip())) < 2:
            flash("El apellido debe tener al menos 2 caracteres para registrarse", "registro")
            es_valido = False

        if usuario['contrasena'] != usuario['contrasena2']:
            flash("Las contraseñas ingresadas no coinciden", "registro")
            es_valido = False

        return es_valido