# Utilice la comprension de listas

lista = []

# Forma normal
for i in range(10):
    lista.append(i * i)
print(lista)

# Forma recomendada
lista2 = [i * i for i in range(10)]
print(lista2)
