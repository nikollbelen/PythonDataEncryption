# Contar las veces que aparece un elemento en una lista

from collections import Counter

lista = [1, 2, 3, 4, 4, 1, 2, 5]
counter = Counter(lista)

print(counter)
print(counter[2])