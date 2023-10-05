import json

def encriptar_mensaje(mensaje: str):
    diccionario = {}

    # Abrir diccionario.json
    with open("diccionario.json") as file:
        diccionario = dict(json.load(file))
    
    mensaje_encriptado = ""
    diccionario = diccionario["palabras"]

    # Iterar a traves de cada letra del mensaje
    for letra in mensaje:
        # Si la letra esta en la cadena, agregar la palabra correspondiente
        if letra.upper() in diccionario:
            mensaje_encriptado += diccionario[letra.upper()] + " "
        # Si la letra no esta agregar la letra original
        else:
            mensaje_encriptado += letra
    return mensaje_encriptado

mensaje = "Hola, esta es una prueb@"
mensaje_encriptado = encriptar_mensaje(mensaje)

# Imprimir mensaje original y encriptado
print(f"Mensaje original: {mensaje}")
print(f"Mensaje encriptado: {mensaje_encriptado}")