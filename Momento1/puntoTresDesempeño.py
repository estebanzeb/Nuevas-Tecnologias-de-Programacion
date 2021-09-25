# 3. Generar un diccionario con los datos de un departamento de Colombia (código, nombre, poblacion,
#    municipios (3 municipios). Luego, mostrar este diccionario, solo con el segundo municipio


departamentos= {
    "cod":"0001",
    "nombre":"Antioquia",
    "Poblacion":5000000,
    "Municipios":
    {
        "medellin": 
        {
            "cod":"0001",
            "nombre":"Medellin",
            "Poblacion":5000000
        },
        
        "bello":
        {
            "cod":"0001",
            "nombre":"Bello",
            "Poblacion":5000000
        },
        "itagui":
        {
            "cod":"0001",
            "nombre":"Itagui",
            "Poblacion":5000000
        }
    }
}


print(departamentos["Municipios"]["medellin"])