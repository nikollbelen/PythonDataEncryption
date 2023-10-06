def operacion(n1, n2, operacion):
    resultado = f"{n1} {operacion} {n2}"
    return eval(resultado) # La funcion eval() resuelve la operacion que esta dentro de una cadena

n1 = input("Ingrese el primer numero: ")
n2 = input("Ingrese el segundo numero: ")
ope = input("Ingrese la operacion: ")

print("-" * 100)
print(f"El resultado es: {operacion(n1, n2, ope)}")