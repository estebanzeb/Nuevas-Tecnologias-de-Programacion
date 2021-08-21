name='Fazt';msg='te pasaste';print(name.upper()+chr(10)+ '¡'+msg.upper()+'!  ;-)')


myStr = "Hello word new"

#Llamar el metodo 
print(dir(myStr))

print(myStr)

#Convertir todo el texto en mayusculas
print(myStr.upper())

#Convertir todo el texto en minusculas
print(myStr.lower())

#Convertir las letras minusculas en mayusculas y viceversa
print(myStr.swapcase())

#Convertir solo la primera letra en mayuscula
print(myStr.capitalize())

#Remplazar el primer texto por el segundo y poner todo en mayusculas
print(myStr.replace('Hello', 'Bye').upper())

#Contar la veces que aparece un caracter
print(myStr.count('l'))

#Validar el caracter que inicia
print(myStr.startswith('hola'))
print(myStr.startswith('Hello'))

#Validar el caracter que finaliza
print(myStr.endswith('hola'))

#Separa los caracteres de una variable
print(myStr.split())

#Buscar la posicion de una caracter
print(myStr.find('o'))
print(myStr.find(' '))
print(myStr.find('w'))

#Contar la catidad de caracteres que tiene esa variable
print(len(myStr))

#
print(myStr.index('w'))

#Validar el tipo de dato
print(myStr.isnumeric())
print(myStr.isalpha())

#Escoger la posicion manualmente
print(myStr[8])

#Concaternar
myStr = "Esteban"
print("Mi Nombre es " + myStr)
print(f"Mi Nombre es {myStr}" )
print("Mi Nombre es {0}".format(myStr))


