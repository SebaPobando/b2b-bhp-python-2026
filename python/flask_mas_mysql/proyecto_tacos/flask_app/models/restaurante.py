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

   def save(cls, datos):
       query = "INSERT INTO restaurantes (nombre, created_at, updated_at) VALUES (%(nombre)s, NOW(), NOW())"
       return connectToMySQL('esquema_tacos').query_db(query, datos)
   
   #Recibimos en un diccionario el id del restaurante que queremos consultar
   @classmethod
   def get_restaurante_y_tacos(cls, datos):
       query = "SELECT * FROM restaurantes LEFT JOIN tacos ON tacos.restaurante_id = restaurantes.id WHERE restaurantes.id = %(id)s;"
       #El resultado es una lista de diccionarios con todos los datos del restaurante perteneciente al id y los tacos relacionados a este
       resultados = connectToMySQL('esquema_tacos').query_db(query, datos)
       #Gracias al LEFT JOIN, sabemos que (independiente de que tenga tacos relacionados) tenemos la información del restaurante, por lo que obtenemos el primer registro de la lista para crear el objeto Restaurante
       restaurante = cls(resultados[0])
       for fila_en_db in resultados:
           #Ahora parseamos los datos del taco para generar instancias de Taco y agregarlas a la lista
           datos_taco = {
               "id": fila_en_db['tacos.id'],
               "tortilla": fila_en_db['tortilla'],
               "guiso": fila_en_db['guiso'],
               "salsa": fila_en_db['salsa'],
               "created_at": fila_en_db['tacos.created_at'],
               "updated_at": fila_en_db['tacos.updated_at'],
           }
           restaurante.tacos.append( taco.Taco(datos_taco)  )

       return restaurante