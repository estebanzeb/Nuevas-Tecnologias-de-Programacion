def GetValorCuota(monto, tasa, cuotas):

    return (monto + (monto * tasa))/cuotas 

monto=float(input("Ingrese el nmonto a prestar: "))
tasa=float(input("Ingrese la tasa del monto: "))
cuotas=float(input("Ingrese el número de cuotas: "))

valorCuota=GetValorCuota(monto, tasa, cuotas)
print(f"el valor de la cuota es de {valorCuota}")