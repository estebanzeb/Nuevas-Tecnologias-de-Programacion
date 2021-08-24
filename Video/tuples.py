#Las tuples son un conjuntos de datos inmutables (osea no se pueden modificar, alterar o cambiar)

x = (1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10)
print (type(x))
print (x)

y = tuple((1,2,3,4))
print (type(y))
print (y)

#print (dir(x))


#Para especificar una dupla de una solo elemento, hay que poner una coma

x = (1, 2, 3, 4, 5)

print (type(x))
print (x)
print (x[3])#Posicion

"""
del x #Eliminar una tupla
print (x)
"""

locations = {
    (35.123213, 39.000): "Tokyo",
    (35.123213, 39.000): "New Yorck"

}
print (locations)