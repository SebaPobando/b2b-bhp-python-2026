import os

# ==========================================
# Crear estructura de proyecto Flask
# ==========================================

def crear_archivo(ruta, contenido=""):
    """Crea un archivo con el contenido indicado."""
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)

def crear_estructura(base_dir="flask_app"):
    # Carpetas principales
    carpetas = [
        f"{base_dir}/config",
        f"{base_dir}/controllers",
        f"{base_dir}/db",
        f"{base_dir}/models",
        f"{base_dir}/static/css",
        f"{base_dir}/static/js",
        f"{base_dir}/static/img",
        f"{base_dir}/templates"
    ]

    # Crear carpetas
    for carpeta in carpetas:
        os.makedirs(carpeta, exist_ok=True)

    # ==========================================
    # __init__.py
    # ==========================================
    crear_archivo(f"{base_dir}/__init__.py", """# ==========================================
# __init__.py
# Inicializa la aplicación Flask
# ==========================================

from flask import Flask

app = Flask(__name__)
app.secret_key = "clave secreta, shhhh!"
""")

    # ==========================================
    # server.py
    # ==========================================
    crear_archivo(f"{base_dir}/../server.py", """from flask_app import app
from flask_app.controllers import main_controller

if __name__ == "__main__":
    app.run(debug=True)
""")

    # ==========================================
    # mysqlconnection.py
    # ==========================================
    crear_archivo(f"{base_dir}/config/mysqlconnection.py", """import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(
            host='localhost',
            user='root',  # Cambia estos valores según tu entorno
            password='root',
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.connection = connection

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                cursor.execute(query, data)
                if query.lower().startswith("insert"):
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().startswith("select"):
                    return cursor.fetchall()
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong:", e)
                return False
            finally:
                self.connection.close()

def connectToMySQL(db):
    return MySQLConnection(db)
""")

    # ==========================================
    # Modelo de ejemplo (con conexión a BD)
    # ==========================================
    crear_archivo(f"{base_dir}/models/example_model.py", """# ==========================================
# example_model.py
# Modelo de ejemplo con conexión a MySQL
# ==========================================
from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    DB = "flask_ejemplo_db"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Guardar un nuevo registro
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, email, created_at, updated_at) VALUES (%(nombre)s, %(email)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)

    # Obtener todos los registros
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL(cls.DB).query_db(query)
        usuarios = []
        for row in results:
            usuarios.append(cls(row))
        return usuarios
""")

    # ==========================================
    # Controlador de ejemplo
    # ==========================================
    crear_archivo(f"{base_dir}/controllers/main_controller.py", """# ==========================================
# main_controller.py
# Controlador de ejemplo con rutas GET y POST
# ==========================================
# from flask_app.config.mysqlconnection import connectToMySQL  # Para consultas directas si se necesita

from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.example_model import Usuario

@app.route('/')
def index():
    usuarios = Usuario.get_all()
    return render_template('index.html', usuarios=usuarios)

@app.route('/crear', methods=['POST'])
def crear_usuario():
    data = {
        "nombre": request.form['nombre'],
        "email": request.form['email']
    }
    Usuario.save(data)
    return redirect('/')
""")

    # ==========================================
    # index.html (con formulario y Jinja)
    # ==========================================
    crear_archivo(f"{base_dir}/templates/index.html", """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Usuarios</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <h1>Gestión de Usuarios</h1>

    <form action="/crear" method="POST">
        <input type="text" name="nombre" placeholder="Nombre" required>
        <input type="email" name="email" placeholder="Correo" required>
        <button type="submit">Agregar</button>
    </form>

    <hr>

    <h2>Lista de usuarios</h2>
    {% if usuarios %}
        <ul>
            {% for u in usuarios %}
                <li>{{ u.nombre }} - {{ u.email }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No hay usuarios registrados.</p>
    {% endif %}

    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
""")

    # ==========================================
    # style.css
    # ==========================================
    crear_archivo(f"{base_dir}/static/css/style.css", """body {
    font-family: Arial, sans-serif;
    background-color: #f8f9fa;
    text-align: center;
    margin-top: 50px;
}

form {
    margin-bottom: 20px;
}

input {
    padding: 8px;
    margin: 5px;
}

button {
    background-color: #007BFF;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

ul {
    list-style: none;
    padding: 0;
}
""")

    # ==========================================
    # script.js
    # ==========================================
    crear_archivo(f"{base_dir}/static/js/script.js", """console.log("Archivo JS cargado correctamente.");
""")

    print(f"\n✅ Estructura Flask con conexión MySQL creada exitosamente dentro de '{base_dir}/'\n")

# ==========================================
# Ejecutar
# ==========================================
if __name__ == "__main__":
    crear_estructura()
