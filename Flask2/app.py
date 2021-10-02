from flask import Flask,render_template, redirect, url_for, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdturismo'

conexion = MySQL(app) # vinculo entre la aplicación y la bd

#Crear la ruta de inicio o home page
@app.route('/') # decorador para la ruta inicio
def inicio():
        
        datosinicio = {
        'menu': 'Inicio',
        'menu2': 'Arma tu plan',
        }
        return render_template('inicio.html', data = datosinicio)

@app.route('/plan') # decorador para la ruta inicio
def plan():
        data = {}
        try:
                cursor = conexion.connection.cursor()
                sql = "SELECT * FROM destino "
                cursor.execute(sql)
                lista = cursor.fetchall()
                # print(companies)
                # data['mensaje'] = 'Exito'
                data['mensaje'] = 'Exito'
                data['lista'] = lista
        except Exception as ex:    
                data['mensaje'] = 'Error ...'
        return render_template('plan.html', destinos = data )

@app.route('/lista') # decorador para la ruta inicio
def lista():
        data = {}
        try:
                cursor = conexion.connection.cursor()
                sql = "SELECT * FROM destino "
                cursor.execute(sql)
                lista = cursor.fetchall()
                # print(companies)
                # data['mensaje'] = 'Exito'
                data['mensaje'] = 'Exito'
                data['lista'] = lista
        except Exception as ex:    
                data['mensaje'] = 'Error ...'
        return jsonify(data) # recordar importar jsonify
# @app.route('/login')
# def login():
#         return render_template('login.html')

# #Intruccion
# def not_found(error):
#         #return render_template('not_found.html'),404
#         return redirect(url_for('index'))

# app.register_error_handler(404, not_found)

# Chequear si estamos en el archivo inicial main
if __name__ == "__main__":
        app.run(debug=True,port=3000) ## para activar modo de depuración para tomar actualizaciones del codigo