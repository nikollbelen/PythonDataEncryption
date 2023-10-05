import string
import random

palabras = {}
palabras["palabras"] = {}
abecedario = list(string.ascii_uppercase) # Creamos una lista con las letras del abecedario en mayuscula
length_of_string = 8

# Llenamos el diccionario con la letra y la palabra correspondiente
for x in abecedario:
  palabra_random = x + ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
  palabras["palabras"][x] = palabra_random

# Transformamos el diccionario en un cadena de texto
palabras = str(palabras)

# Reemplazamos las comillas simples por las dobles
palabras = palabras.replace("'", '"')

# Llenamos el archivo json
with open("diccionario.json", "a") as file:
    file.write(palabras)
