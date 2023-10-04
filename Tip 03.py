# Ordenar iterables complejos

data = [
    {"nombre": "Harry Potter", "edad": 15},
    {"nombre": "Hermione Granger", "edad": 19},
    {"nombre": "Ron Weasly", "edad": 4},
    {"nombre": "Luna LoveHood", "edad": 20},
]

# Forma recomendada
data_ordenada2 = sorted(data, key = lambda x: x["edad"])
print(data_ordenada2)