# from flask import Flask

# app=Flask(__name__)

# 	#__name__ es un workspace

# 	# "__main__" es el nombre del ámbito en el que se ejecuta el 
# 	# código de nivel superior (tu programa principal)

# 	# El intérprete pasa el valor del atributo __name__ a la cadena '__main__'

# 	# Chequear si estamos en el archivo inicial main
# if __name__ == "__main__":
#     app.run()

from flask import Flask,render_template

app=Flask(__name__)

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
        'referencias': ['2','Aveo', 'Logan', '5 power','Airton'],
        'colores': ['azul', 'yellowo', 'redy', 'bluck', 'nigga'],
        'cantvehiculos': len(vehiculos)
        }
        return render_template('index.html', data = datosindex)

@app.route('/login')
def login():
        return render_template('login.html')



# Chequear si estamos en el archivo inicial main
if __name__ == "__main__":
        app.run(debug=True,port=5200) ## para activar modo de depuración para tomar actualizaciones del codigo