from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = '123123234831983182'

@app.route('/')
def holamundo():
    if 'visitas' in session:
        print("Existe esa propiedad en sesión")
        session['visitas'] += 1
        print(session['visitas'])
    else:
        print("No existe la propiedad")
        session['visitas'] = 0
        print("Ahora visitas existe en session.")
    
    return render_template('index.html', visitas = session['visitas'])

@app.route('/destruir_sesion')
def destruir_sesion():
    session.clear()
    return redirect('/')

@app.route('/aumentar_dos', methods=['POST'])
def aumentar_dos():
    if 'visitas' in session:
        session['visitas'] += 1
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)