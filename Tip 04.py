# Definir valores predeterminados en diccionarios

my_dict = {"nombre": "Harry", "apellido": "Potter"}

# Forma normal
# apellido = my_dict["edad"]

# Forma recomendada
apellido = my_dict.get("edad", "NO EXISTE")
print(apellido)