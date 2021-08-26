from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Aprendiendo Flask"

@app.route('/informacion')
@app.route('/informacion/<string:nombre>')
def informacion(nombre = None):

    texto = ""

    if nombre != None:
        texto = f"<h3>Bienvenido , {nombre}</h3>"
    
    return  f"""
        <h1> Pagina de informacion </h1>
        <p>
        Esta es la pagina de informacion del creador del sistio
        <p>
       {texto}
"""

@app.route('/contacto')
def contacto():
    return "<h1>Contacto</h1>"

@app.route('/lenguajes')
def lenguajes():
    return "<h1>lenguajes</h1>"

if __name__ == '__main__':
    app.run(debug=True)

