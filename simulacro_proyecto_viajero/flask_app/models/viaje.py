from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime, date

class Viaje:
    def __init__(self, data):
        self.id = data['id']
        self.destino = data['destino']
        self.fecha_inicio = data['fecha_inicio']
        self.fecha_fin = data['fecha_fin']
        self.itinerario = data['itinerario']
        self.organizador_id = data['organizador_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #campos extra -- nos pueden ayudar a encontrar informacion mas facil
        self.organizador_nombre = data.get('organizador_nombre','')
        #self.viajeros = [] # lista de usuarios incritas -- BONUS

    @classmethod
    def save(cls, data):
        query = """INSERT INTO viajes (destino, fecha_inicio, fecha_fin, itinerario, organizador_id)
                   VALUES (%(destino)s,%(fecha_inicio)s,%(fecha_fin)s,%(itinerario)s, %(organizador_id)s);
                """
        return connectToMySQL('esquema_viajero_frecuente').query_db(query, data)

    @classmethod
    def get_all_valid_trips(cls):
        query = """SELECT viajes.*, CONCAT(usuarios.nombre, ' ', usuarios.apellido) AS organizador_nombre
                   FROM viajes
                   JOIN usuarios ON viajes.organizador_id = usuarios.id
                   WHERE viajes.fecha_inicio >= CURDATE()
                   ORDER BY viajes.fecha_inicio ASC;
                """
        results = connectToMySQL('esquema_viajero_frecuente').query_db(query)
        viajes = []
        if results:
            for r in results:
                viajes.append(cls(r))
        return viajes
