from rembg import remove
from PIL import Image

quitar_fondo = remove(Image.open("img.png")) # Remover el fondo 
quitar_fondo.save("img_sin_fondo.png") # Guarda la nueva imagen sin fondo