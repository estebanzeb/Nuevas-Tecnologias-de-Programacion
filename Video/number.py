#Tipos de numeros
print (type(9))
print (type(14.4))

#Operaciones matematicas 
print(5+5)
print(5*5)
print(5/5)
print(5-5)

#Exponente
print(5**2)

#Saber el reciduo de una division
print(5//5)

print(5+5-8*2+10**2)
print((5+5-8)*2+(10**2))

#Pedir que se inserte un dato
age = input("Inset your age: ") # Cada vez se inserte algo siempre sera de tipo string
print(type(age))
#Se convierte en entero para poder sumar
agesum = int(age) + 10
print(agesum)

#Cambiar o convierte un tipo de dato
age = "22"
print(type(age))
print(age)
print(type(int(age)))
print(age)
print(type(float(age)))
print(age)