import cv2

# Especificar la ruta de la imagen original
imagen = cv2.imread("img.png")
nombre_ventana = "Imagen original"

# Mostrar la imagen original en una ventana
cv2.imshow(nombre_ventana, imagen)

# Convertir la imagen de un color a otro
img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
color_invertido = cv2.bitwise_not(img_gris)

# Suavizar la imagen
desenfoque = cv2.GaussianBlur(color_invertido, (21, 21), 0)
desenfoque_invertido = cv2.bitwise_not(desenfoque)
dibujo = cv2.divide(img_gris, desenfoque_invertido, scale = 256.0)

# Guardar la imagen convertida
cv2.imwrite("img-dibujo.png", dibujo)

# Leer la imagen nueva
imagen = cv2.imread("img-dibujo.png")
nombre_ventana = "Imagen en dibujo"

# Mostrar la imagen en dibujo en una ventana
cv2.imshow(nombre_ventana, imagen)

# Esperar a que el usuario presione una tecla,
# Para evitar que el kernel de Python se bloquee
cv2.waitKey(0)

# Cerrar todas las pestañas
cv2.destroyAllWindows()