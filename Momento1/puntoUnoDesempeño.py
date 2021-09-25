# 1. Crear una lista con 5 municipios del departamento de Antioquia. Luego, recorrer esta lista y mostrar
# cada ciudad excepto una de ellas (cualquiera).


i=1
x=0

lista = []
while i <= 5:
    ciudad=input(f"ciudad {i} a ingresar: ")        
    lista.append(ciudad)
    i += 1             


cant=int(input("numero de ciudad a retirar (numero del 0 al 4): "))

for ciu in lista:  
    if   x == cant:
        print("Eliminado")
    else:
        print(lista[x])
    x=x+1