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
       
    # AGREGAR MÉTODOS DE VALIDACIÓN
