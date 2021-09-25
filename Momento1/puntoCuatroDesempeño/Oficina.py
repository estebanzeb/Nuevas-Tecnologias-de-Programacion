# 4. Generar los archivos necesarios para generar las clases, con base en el siguiente diagrama:
# Inmueble

from Inmueble import Inmueble

class Oficina(Inmueble):
    def __init__(self, salaAsamblea):
        self.salaAsamblea = salaAsamblea


    def instalarInternet(self):
        # Método vacío
        return Inmueble.__str__(self) + "instalar internet"

