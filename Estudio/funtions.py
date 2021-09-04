#def hace referencia a una funcion

def hello(name="Person"):
    print ("Hello Word " + name )

hello("Esteban")
hello("Joe")
hello("Lola")
hello()

def add(numberOne, numberTwo):
    return numberOne + numberTwo

print (add(10, 30),"\n")

#funtion lambda
add = lambda numberOne, numberTwo: numberOne + numberTwo

print (add(10, 30))