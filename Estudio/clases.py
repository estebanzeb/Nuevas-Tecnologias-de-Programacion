def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

class MiClase:
    
    def __init__(self):
        self._atributo_privado = 1
    
    def _metodo_privado(self):
        print("Hola mundo!")


mi_objeto = MiClase()
print(mi_objeto._atributo_privado)
mi_objeto._metodo_privado()

class Alumno:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        """Imprime un saludo en pantalla."""
        print(f"¡Hola, {self.nombre}!")


alumno = Alumno("Esteban")
alumno.saludar()

class Rectangulo:
    """
    Define un rectángulo según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h

rectangulo = Rectangulo(20, 10)
print("Área del rectángulo: ", rectangulo.area(),"\n")

#------------------------------------------------------------------------
class Triangulo:
    """
    Define un triángulo según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return (self.b * self.h) / 2

triangulo = Triangulo(20, 12)
print("Área del triangulo: ", triangulo.area(),"\n")

#------------------------------------------------------------------------

class Poligono:
    """
    Define un polígono según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h

class Rectangulo(Poligono):

    def area(self):
        return self.b * self.h

class Triangulo(Poligono):

    def area(self):
        return (self.b * self.h) / 2

rectangulo = Rectangulo(20, 10)
triangulo = Triangulo(20, 12)

print("Área del rectángulo: ", rectangulo.area(),"\n")
print("Área del triángulo:", triangulo.area(),"\n")

#----------------------------------------------------------------

class MiClase:
    
    def __init__(self):
        self._atributo_privado = 1
    
    def _metodo_privado(self):
        print("Hola mundo!")


mi_objeto = MiClase()
print(mi_objeto._atributo_privado)
mi_objeto._metodo_privado()

#----------------------------------------------------------------


class Car:
    #Son metoddos
    def __init__(self,marca):
        self.marca = marca
        #print("Soy un nuevo objeto")
    #Son metoddos
    def prender(self, mensaje):
        print (mensaje)

carro = Car("Renol")
carro2 = Car("Mazda")

print ("La marca del carro es" , carro.marca)

print ("La marca del carro es" , carro2.marca)

carro.prender("Encender le carro")

