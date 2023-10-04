# Iterar con enumerate() en lugar de range(len())

data = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete"]

# Forma normal
for i in range(len(data)):
    print(i, data[i])

print("*" * 100)

# Forma recomendada
for idx, num in enumerate(data):
    print(idx, num)