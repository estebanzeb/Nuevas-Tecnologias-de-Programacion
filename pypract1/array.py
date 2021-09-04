# Importar módulo array
import array

# Declarar lista con valores numéricos
lista1 = [1, 0, 1, 0, 1, 1, 0, 0]

# Obtener cadena con todos los tipos de arrays disponbiles
array.typecodes  # 'bBuhHiIlLqQfd'

# Declarar 'array1' de tipo 'char sin signo' con datos de 'lista1'
array1 = array.array('B', lista1)

# Obtener tipo de array y datos de 'array1'
print (array1)  # array('B', [1, 0, 1, 0, 1, 1, 0, 0])