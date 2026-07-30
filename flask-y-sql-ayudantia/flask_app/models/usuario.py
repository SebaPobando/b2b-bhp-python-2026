# Importamos la función que devolverá una instancia de una conexión
from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL('esquema_usuarios').query_db(query)

        usuarios = []

        for usuario in resultados:
            usuarios.append(cls(usuario))

        return usuarios

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, apellido, email) VALUES(%(nombre)s, %(apellido)s, %(email)s);"
        return connectToMySQL('esquema_usuarios').query_db(query, datos)