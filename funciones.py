def mensaje():
    print("Hola desde la funcion mensaje\n")

def sumar(a,b):
    return a + b

def calculatesalary (nht,vh):
    salary = 0
    if nht >= 204:
        salary = nht * vh
    return salary

def empenable(nht):
    active = True
    if nht == 0:
        active = False
    return active

mensaje()

print(sumar(2, 2),"\n")

print(calculatesalary(205, 300))




def saludar(funtion):
    print('Antes de la ejecución de la función a decorar')
    funtion()
    print('Después de la ejecución de la función a decorar')  
    return funtion

@saludar
def despedir():
    print("Bye")





