# from flask import Flask

# app=Flask(__name__)

# 	#__name__ es un workspace

# 	# "__main__" es el nombre del ámbito en el que se ejecuta el 
# 	# código de nivel superior (tu programa principal)

# 	# El intérprete pasa el valor del atributo __name__ a la cadena '__main__'

# 	# Chequear si estamos en el archivo inicial main
# if __name__ == "__main__":
#     app.run()

from flask import Flask,render_template, redirect, url_for, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect

from flask_mysqldb import MySQL
app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbdflask'

conexion = MySQL(app) # vinculo entre la aplicación y la bd

#endpoints o rutas
@app.route('/companies')
def list_cars():
        data = {}
        try:
                cursor = conexion.connection.cursor()
                sql = "SELECT id, marca, moderlo,valor, FROM car ORDER BY marca"
                cursor.execute(sql)
                cars = cursor.fetchall()
                # print(companies)
                # data['mensaje'] = 'Exito'
                data['cars'] = cars
        except Exception as ex:    
                data['mensaje'] = 'Error ...'
        return jsonify(data) # recordar importar jsonify

#Crear la ruta de inicio o home page
@app.route('/') # decorador para la ruta inicio
def index():
        #return '<h1>HInicio desde la ruta</h1>'
        vehiculos = ['Mazda', 'Chevrolet',' Renault', 'Audi', 'ferrari']
        datosindex = {
        'titulo': 'Sistema de Prueba',
        'subtitulo': 'Bienvenido al sistema ususario',
        'vehiculos': vehiculos,
        'usuario': 'usuarioPrueba',
        'referencias': ['2','Aveo', 'Logan', 'power','Airton'],
        'colores': ['azul', 'yellowo', 'redy', 'bluck', 'nigga'],
        'cantvehiculos': len(vehiculos)
        }
        return render_template('index.html', data = datosindex)

@app.route('/login')
def login():
        return render_template('login.html')

#Intruccion
def not_found(error):
        #return render_template('not_found.html'),404
        return redirect(url_for('index'))

app.register_error_handler(404, not_found)

# Chequear si estamos en el archivo inicial main
if __name__ == "__main__":
        app.run(debug=True,port=5200) ## para activar modo de depuración para tomar actualizaciones del codigo