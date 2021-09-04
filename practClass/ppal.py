from transporte.vehiculo import Vehiculo
from transporte.automovil import Automovil

veh1 = Vehiculo("48150", 9, 2)
auto = Automovil("48150", 9, 2, False, 5)

print(f"El numero de asientos es: {veh1.GetNroasientos()}")

#veh1.SetNromasientos(8)

print(f"La guantera esta: {(auto.Getguantera())}")