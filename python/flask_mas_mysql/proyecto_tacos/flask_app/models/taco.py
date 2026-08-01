from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import complemento

class Taco:
    def __init__(self, data):
        self.id = data['id']
        self.tortilla = data['tortilla']
        self.guiso = data['guiso']
        self.salsa = data['salsa']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Usamos .get() porque en algunos JOIN no traemos estas columnas
        self.restaurante_id = data.get('restaurante_id')
        self.nombre_restaurante = data.get('nombre_restaurante')
        # Lista para guardar los complementos asociados al taco
        self.complementos = []

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO tacos (tortilla, guiso, salsa, restaurante_id) VALUES(%(tortilla)s, %(guiso)s, %(salsa)s, %(restaurante_id)s);"
        return connectToMySQL('esquema_tacos').query_db(query, datos)

    @classmethod
    def get_all(cls):
        # Traemos también el nombre del restaurante con un alias para poder mostrarlo
        query = "SELECT tacos.*, restaurantes.nombre AS nombre_restaurante FROM tacos JOIN restaurantes ON tacos.restaurante_id = restaurantes.id;"
        tacos_en_bd = connectToMySQL('esquema_tacos').query_db(query)
        tacos = []
        if tacos_en_bd:
            for taco in tacos_en_bd:
                tacos.append(cls(taco))
        return tacos

    @classmethod
    def get_one(cls,datos):
        query = "SELECT tacos.*, restaurantes.nombre AS nombre_restaurante FROM tacos JOIN restaurantes ON tacos.restaurante_id = restaurantes.id WHERE tacos.id = %(id)s;"
        taco_en_db = connectToMySQL('esquema_tacos').query_db(query,datos)
        if not taco_en_db:
            return None
        return cls(taco_en_db[0])

    # Trae un taco junto con la lista de complementos que tiene asociados
    @classmethod
    def get_taco_con_complementos(cls, datos):
        query = "SELECT * FROM tacos LEFT JOIN complementos_en_tacos ON complementos_en_tacos.taco_id = tacos.id LEFT JOIN complementos ON complementos_en_tacos.complemento_id = complementos.id WHERE tacos.id = %(id)s;"
        resultados = connectToMySQL('esquema_tacos').query_db(query, datos)
        if not resultados:
            return None
        taco = cls(resultados[0])
        for fila_en_db in resultados:
            # Si el taco no tiene complementos, esas columnas vienen en NULL
            if fila_en_db['nombre_complemento'] is None:
                break
            datos_complemento = {
                "id": fila_en_db['complementos.id'],
                "nombre_complemento": fila_en_db['nombre_complemento'],
                "created_at": fila_en_db['complementos.created_at'],
                "updated_at": fila_en_db['complementos.updated_at'],
            }
            taco.complementos.append( complemento.Complemento(datos_complemento) )
        return taco

    @classmethod
    def update(cls, datos):
        query = "UPDATE tacos SET tortilla=%(tortilla)s, guiso=%(guiso)s, salsa=%(salsa)s, restaurante_id=%(restaurante_id)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('esquema_tacos').query_db(query, datos)

    @classmethod
    def delete(cls, datos):
        query = "DELETE FROM tacos WHERE id = %(id)s;"
        return connectToMySQL('esquema_tacos').query_db(query, datos)
