# Combinar diccionarios

d1 = {"nombre": "Harry", "edad": "Potter"}
d2 = {"nombre": "Harry", "ciudad": "New York"}

combinacion = {**d1, **d2}
print(combinacion)