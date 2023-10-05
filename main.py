import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Definir las credenciales
remitente = 'alicialopezjara585@gmail.com'
password = 'wobr xqbl gxwu znik'

# Definir los detalles del destinatario
destinatario = "nikoll.bonilla.hancco@gmail.com"
asunto = "Prueba de correo"

# Crear el mensaje
mensaje = MIMEMultipart()
mensaje["From"] = remitente
mensaje["To"] = destinatario
mensaje["Subject"] = asunto

# Agregar el cuerpo del mensaje
cuerpo = "Este es el cuerpo del email"
mensaje.attach(MIMEText(cuerpo, "plain"))

# Iniciar sesion en servidor SMTP de gmail
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(remitente,password)

# Enviar correo 
texto = mensaje.as_string()
server.sendmail(remitente, destinatario, texto)
server.quit()

print("Correo enviado")