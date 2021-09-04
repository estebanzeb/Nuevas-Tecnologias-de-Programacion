class Vehículo:
    
    def __init__(self,marca,modelo,placa,valor,color):
        self._marca = marca
        self._modelo = modelo
        self._placa = placa 
        self._valor = valor
        self._color = color
    
    def _metodo_privado(self):
        print("Hola mundo!")


mi_objeto = Vehículo("Apple","2030","AB4-P54","Estados Unidos",100000000000)
print(mi_objeto._marca)
mi_objeto._metodo_privado()