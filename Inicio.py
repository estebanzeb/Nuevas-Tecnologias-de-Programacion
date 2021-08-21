print("Hello word bith")
a = 2500
b = "Feria de Flores"
c = True
d= [12, 45, 67, 89, 120, 23]

[12, 45, 67, 89, 120, 23]
#diccionaria
datosemp = {"Cedula":"43","Nombre":"Permitame Dios", "Telefono":["2291100", "3124567890"]}

print(datosemp)

"""
 Este es un comentario de
 varias lineas

"""

print("Evento papa",b,end='')

print(" en la ciudad de Medellín")

print("\n\n\n\n Texto de prueba con saltos de linea \n\n")

print(f"Evento que se celebra en Medellín {b} en el mes de Agosto")

#Condicional

if a > 2300 and not c :
    print("Tiene derecho a bono de feriacion")
    print("Visita las fondas de mi tierra")
else: 
    print("No tiene derecho a bono de la feriencion")


categoria = "A"
valorcopago = 0

if categoria == "A":
    valorcopago = 5000
elif categoria == "B":
    valorcopago = 7500
elif categoria == "C":
    valorcopago = 10000
elif categoria == "D":
    valorcopago = 12500
else:
    valorcopago = 1200
print(f"El valor del copago es : {valorcopago}")

#Operador ternario
estado = "Activo" if not c else "Inactivo"

print(estado)

i = 1

while i < 10:
   print (f"El resultado de 3 x {i}  es  {i*3}")
   i += 1

for nro in d:
    print(d)

for letra in "CESDE":
    print(letra,end='')    

for nro in range(6):
    print(nro)

for nro in range(20,31):
    print(nro)

for e in range(40,81):
    print(e)

#Mostrar datos del diccionario datosemp

datosemp = {"cedula":"1020490155","nombre":"Esteban Quintero Yepes", "telefono":["4764060", "3124567890"]}


print(f"cedula: {datosemp['cedula']}".capitalize())
print(f"nombre: {datosemp['nombre']}".capitalize())
print(datosemp,"\n")

for key in datosemp:
    print(key, ":", datosemp[key],"\n")

print("telefono fijo: ".capitalize(),datosemp['telefono'][0])
print("telefono movil: ".capitalize(),datosemp['telefono'][1])

#Capturar datos por teclado
valor = float(input("Inserte el número de horas: "))
print(valor*3000)