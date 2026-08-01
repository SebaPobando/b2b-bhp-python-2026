from flask_app.config.mysqlconnection import connectToMySQL #importamos desde config
from flask_app.models import taco

class Restaurante:
   def __init__(self, data):
       self.id = data['id']
       self.nombre = data['nombre']
       self.created_at = data['created_at']
       self.updated_at = data['updated_at']
       #Creamos una lista vacía para luego agregar todos los tacos relacionados con el restaurante
       self.tacos = []

   @classmethod
   def save(cls, datos):
       query = "INSERT INTO restaurantes (nombre, created_at, updated_at) VALUES (%(nombre)s, NOW(), NOW());"
       return connectToMySQL('esquema_tacos').query_db(query, datos)

   @classmethod
   def get_all(cls):
       query = "SELECT * FROM restaurantes;"
       restaurantes_en_db = connectToMySQL('esquema_tacos').query_db(query)
       restaurantes = []
       if restaurantes_en_db:
           for restaurante in restaurantes_en_db:
               restaurantes.append(cls(restaurante))
       return restaurantes

   @classmethod
   def get_one(cls, datos):
       query = "SELECT * FROM restaurantes WHERE id = %(id)s;"
       resultados = connectToMySQL('esquema_tacos').query_db(query, datos)
       if not resultados:
           return None
       return cls(resultados[0])

   @classmethod
   def update(cls, datos):
       query = "UPDATE restaurantes SET nombre = %(nombre)s, updated_at = NOW() WHERE id = %(id)s;"
       return connectToMySQL('esquema_tacos').query_db(query, datos)

   @classmethod
   def delete(cls, datos):
       query = "DELETE FROM restaurantes WHERE id = %(id)s;"
       return connectToMySQL('esquema_tacos').query_db(query, datos)

   #Recibimos en un diccionario el id del restaurante que queremos consultar
   @classmethod
   def get_restaurante_y_tacos(cls, datos):
       query = "SELECT * FROM restaurantes LEFT JOIN tacos ON tacos.restaurante_id = restaurantes.id WHERE restaurantes.id = %(id)s;"
       #El resultado es una lista de diccionarios con todos los datos del restaurante perteneciente al id y los tacos relacionados a este
       resultados = connectToMySQL('esquema_tacos').query_db(query, datos)
       if not resultados:
           return None
       #Gracias al LEFT JOIN, sabemos que (independiente de que tenga tacos relacionados) tenemos la información del restaurante, por lo que obtenemos el primer registro de la lista para crear el objeto Restaurante
       restaurante = cls(resultados[0])
       for fila_en_db in resultados:
           #Si el restaurante todavía no tiene tacos, el LEFT JOIN devuelve esas columnas en NULL
           if fila_en_db['tacos.id'] is None:
               break
           #Ahora parseamos los datos del taco para generar instancias de Taco y agregarlas a la lista
           datos_taco = {
               "id": fila_en_db['tacos.id'],
               "tortilla": fila_en_db['tortilla'],
               "guiso": fila_en_db['guiso'],
               "salsa": fila_en_db['salsa'],
               "created_at": fila_en_db['tacos.created_at'],
               "updated_at": fila_en_db['tacos.updated_at'],
               "restaurante_id": fila_en_db['restaurante_id'],
           }
           restaurante.tacos.append( taco.Taco(datos_taco)  )

       return restaurante
