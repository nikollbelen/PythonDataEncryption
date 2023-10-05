# FILTER
#  Filtrar numeros impares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = list(filter(lambda x: x % 2 != 0 , numeros))
print(impares)
print("-" * 100)

# MAP
#  Elevar al cuadrado los numeros de una lista
cuadrados = list(map(lambda y: y**2, numeros))
print(numeros)
print("-" * 100)

# REDUCE
#  Sumar todos los numeros de una lista
from functools import reduce

suma = reduce(lambda x, z: x + z, numeros)
print(suma)