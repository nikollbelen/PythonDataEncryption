# Concatenar cadenas con .join()

lista_cadenas = ["Hello", "my", "friend"]

# Forma normal
mi_cadena1 = ""
for i in lista_cadenas:
    mi_cadena1 += i + " "

print(mi_cadena1)

# Forma recomendada
mi_cadena2 = " ".join(lista_cadenas)
print(mi_cadena2)