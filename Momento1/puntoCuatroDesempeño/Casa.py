# 4. Generar los archivos necesarios para generar las clases, con base en el siguiente diagrama:
# Inmueble

from Inmueble import Inmueble


class Casa(Inmueble):

    def __init__(self, nroHabitaciones):
        self.nroHabitaciones = nroHabitaciones

    def repararJardin(self):
        # Método vacío
        return Inmueble.__str__(self) + " - esta llamando una funcion de la casa (reparar Jardin)"

