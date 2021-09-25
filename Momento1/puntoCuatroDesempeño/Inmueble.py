# 4. Generar los archivos necesarios para generar las clases, con base en el siguiente diagrama:
# Inmueble

class Inmueble():
    def __init__(self, codigo, direccion,telefono):
        self.codigo = codigo
        self.direccion = direccion
        self.telefono = telefono


    def __str__(self):
        return "Esta llamando una funcion del inmueble"

 
    def radicar(self):
        # Método vacío
        return "radicar"


    def arrendar(self):
        # Método vacío
        return "arrendar"



