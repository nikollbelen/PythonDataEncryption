import gofile as go 

def subir_archivo(archivo):
    cur_server = go.getServer()
    print(f"El servidor es: {cur_server}")

    url_descarga = go.uploadFile(archivo)
    print(f"El link del archivo subido es: {url_descarga['downloadPage']}")

subir_archivo("imagen.png")