demo_list = [1, "Hello", 1.34, True,[1, 2, 3, 4, 5]]

colors = ['red', 'green', 'blue', 'yellow']

#Constructor con lista
numbers_list = list((1, 2, 3, 4))
print (type(numbers_list))
print (numbers_list)

#Rangos
r = list(range(1, 1001))
print (type(r))
print (r)

print (type(colors))
#Que puedo hacer e una lista DIR
print (dir(colors))
print (colors)
#Cantidad de la lista 
print (len(colors),"\n")
print (len(demo_list),"\n")
#Indeces de una lista
print (colors[1])
#Saber si hay un elmento en la lista
print ('green' in colors)
print ('purple' in colors)

#Cambiar los datos que estan en la lista
print (colors)
colors[1] = 'pink'
print (colors)

#rint (dir(colors))

colors.append('violet')
#Tupla
colors.append(['white', 'black'])
#Lista
colors.append(('white', 'black'))

print (colors,"\n")

#extend puedes pasarle una lista o tupla y los resive por separado
#Tupla
colors.extend(['blue', 'red'])
print (colors,"\n")
#lista
colors.extend(('white', 'black'))
print (colors,"\n")

#Insertar en una posicion especifica
colors.insert(1,'grey')#-1 sera el ultimo

print (colors,"\n")

colors.insert(len(colors),'grey')
print (colors,"\n")

#Quitar una valor especifico (Primero va remove antes de pop)
colors.remove('pink')

colors.pop()
print (colors,"\n")

#Quitar por posicion
colors.pop(3)
print (colors,"\n")

colors.clear()
print (colors,"\n")

colors = ['red', 'green', 'blue', 'yellow', 'red']

#Ordenar alfabeticamente
colors.sort()
print (colors,"\n")

#Ordenar a la inversa
colors.sort(reverse=True)
print (colors,"\n")

#Obtener al posicion
print(colors.index('blue'))

#Contar la cantidad de datos que hay
print(colors.count('green'))