from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/')
def holamundo():
    return "Hola mundo!"

@app.route('/juego/<int:cantidad>')
def juego(cantidad):
    return render_template('juego.html', cantidad=cantidad)

if __name__ == "__main__":
    app.run(debug=True)