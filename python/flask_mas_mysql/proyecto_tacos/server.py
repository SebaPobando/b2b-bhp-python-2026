from flask_app import app #Importamos la app de la carpeta flask_app
from flask_app.controllers import tacos #Importamos los controladores
from flask_app.controllers import restaurantes
from flask_app.controllers import complementos

if __name__=="__main__": #Ejecutamos la aplicación

   app.run(debug=True)