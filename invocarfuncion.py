from funciones import  sumar,mensaje,calculatesalary,saludar, empenable

mensaje()

print(sumar(2, 2),"\n")

#mysalary = calculatesalary(240,3785)
mysalary = calculatesalary(0,10000)


# if mysalary > 0:
#     print(mysalary)
# else:
#     print("Valores invalidos para calcular el salario")

print(mysalary if mysalary > 0 else "Valores invalidos para calcular el salario")
if not empenable(0):
    print("El empleado esta inactivo")

#despedir()