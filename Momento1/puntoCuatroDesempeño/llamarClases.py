from Oficina import Oficina
from Casa import Casa
from Inmueble import Inmueble

inmueble = Inmueble("codigo","direccion","telefono")
print(inmueble.radicar())

casa = Casa(4)
print(casa.repararJardin())


oficina = Oficina("si")
print(oficina.instalarInternet())