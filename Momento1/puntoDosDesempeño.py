# 2. Generar una lista con los 10 primeros de la siguiente sucesión: 7,11,15,19,23…


numeroInicial = 7
constante = 4
i=0


lista = []
lista.append(numeroInicial)
while i < 10:      

    numeroInicial += 4
    lista.append(numeroInicial)
    i += 1     
    
print(lista)
