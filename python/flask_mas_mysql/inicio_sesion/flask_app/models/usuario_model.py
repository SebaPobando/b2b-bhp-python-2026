from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    db = "esquema_sesion"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.email = data['email']
        self.password = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Guardar un nuevo registro
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, email, created_at, updated_at) VALUES (%(nombre)s, %(email)s, NOW(), NOW());"
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
