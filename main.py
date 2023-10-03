import sqlite3

# Conexion a la base de datos
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        email TEXT
    )"""
)

conn.commit()

# Crear registro -> C
def crear_usuario(nombre:str, email) -> str:
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES(?, ?)", (nombre, email))
    conn.commit()
    return "Usuario agregado"

# Obtener usuarios -> R
def obtener_usuarios() -> list:
    cursor.execute("SELECT id, nombre, email FROM usuarios")
    usuarios = cursor.fetchall()

    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append(usuario)

    return lista_usuarios

# Actualizar usuario por su id -> U
def actualizar_usuario(id, nombre, email):
    cursor.execute("UPDATE usuarios SET nombre=?, email=? WHERE id = ?", (nombre,email,id))
    conn.commit()
    return "Usuario actualizado"

# Eliminar usuario -> D
def eliminar_usuario(id) -> str:
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    return "Usuario eliminado"

# Leer registro con su id
def obtener_usuario(id: int):
    cursor.execute("SELECT id, nombre, email FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()

    if usuario:
        return usuario
    return "Usuario no encontrado"

# Crear usuarios -> C
# crear_usuario("Harry", "harry@gmail.com")
# crear_usuario("Ron", "ron@gmail.com")
# crear_usuario("Hermione", "hermione@gmail.com")

# Obtener usuarios -> R
print(obtener_usuarios())

# Actualizar usuarios -> U
#print(actualizar_usuario("3", "Ron2", "ron2@gmail.com"))

# Eliminar usuario -> D
print(eliminar_usuario(6))