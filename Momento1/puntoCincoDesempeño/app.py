from flask import Flask,render_template
app = Flask(__name__)

# endpoint o rutas
@app.route('/')
def index():
    #return "<h1>Hola, desde la página de incio</h1>"
    vehiculos = ['Mazda','Chevrolet','Renault','Audi','Ferrari']
    datosindex = {
        'titulo':'Sistema de Prueba',
        'subtitulo':'Esto es un mensaje de prueba para el taller del momento numero 1: ',
        'usuario':'Andres Felipe Perez Osorno',

    }
    return render_template('index.html',data = datosindex)

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/maestra')
def maestra():
    return render_template('maestra.html')


if __name__ == "__main__":
    app.run(debug=True, port=3200)