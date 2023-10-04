# Simplificar las declaraciones de condicionales con if x  in list

colores = ["rojo", "verde", "amarillo"]

# Forma normal
c = "rojo"

if c == "rojo" or c == "verde" or c == "amarillo":
    print("El rojo esta alli")

# Forma recomendada
if c in colores:
    print("El rojo esta alli")