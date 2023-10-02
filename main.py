from cryptography.fernet import Fernet

def generar_clave():
  return Fernet.generate_key()

def encriptar_texto(texto, clave):
  f = Fernet(clave)
  texto_encriptado = f.encrypt(texto.encode())
  return texto_encriptado

def desencriptar_texto(texto_encriptado, clave):
  f = Fernet(clave)
  texto_desencriptado = f.decrypt(texto_encriptado).decode()
  return texto_desencriptado

# Se genera una clave

clave_secreta = generar_clave()
print("*"*20)
print(f"Clave secreta: {clave_secreta}")

# Se crea el texto

texto = "Esta es una informacion de suma importancia"
print("*"*20)
print(f"Texto: {texto}")

# Se encripta el texto

texto_encriptado = encriptar_texto(texto, clave_secreta)
print("*"*20)
print(f"Texto encriptado: {texto_encriptado}")

# Se desencripta el texto

texto_desencriptado = desencriptar_texto(texto_encriptado, clave_secreta)
print("*"*20)
print(f"Texto desencriptado: {texto_desencriptado}")
