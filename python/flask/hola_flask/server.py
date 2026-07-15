from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def hola_mundo():
#    return '¡Hola Mundo!'

# @app.route('/chao')
# def chao_mundo():
#     return '¡Chao Mundo!'

# @app.route('/exito')
# def exito():
#    return "¡Éxito!"

# @app.route('/saludo/<nombre>')
# def saludo(nombre):
#    print(nombre)
#    return (f'¡Hola {nombre}!')

# @app.route('/color/<nombre>/<color>')
# def color_favorito(nombre, color):
#    print(nombre)
#    print(color)
#    return f'Hola {nombre}, tu color favorito es el {color}'

# @app.route('/saludo/<nombre>/<int:num>')
# def hola_cantidad(nombre, num):
#    return f'¡Hola {nombre}!'*num

@app.route('/')
def hola_flask():
    return '¡Hola desde Flask!'
    
@app.route('/ruta')
def ruta():
    return '¿Qué ruta estás buscando?'

@app.route('/bienvenido/python')
def bienvenido_python():
    return 'Bienvenid@ a esta ruta Python'

@app.route('/bienvenido/miyagi')
def bienvenido_miyagi():
    return 'Bienvenid@ a esta ruta Miyagi'

@app.route('/bienvenido/taquito')
def bienvenido_taquito():
    return 'Bienvenid@ a esta ruta Taquito'

@app.route('/repite/<int:num>/hola')
def repite_hola(num):
    return 'Repite después de mi: ' + ' hola'*num
    
@app.route('/repite/<int:num1>/adios')
def repite_adios(num1):
    return 'Repite después de mi:' + ' adios'*num1

@app.route('/repite/<int:num2>/divertido')
def repite_divertido(num2):
    return 'Repite después de mi:' + ' divertido'*num2

if __name__=="__main__":
   app.run(debug=True)