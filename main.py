import asyncio

# Definimos la primera tarea asincrona
async def tarea_1():
    print("Tarea 1 iniciada")
    await asyncio.sleep(1) # Esperar un segundo
    print("Tarea 1 finalizada")

async def tarea_2():
    print("Tarea 2 iniciada")
    await asyncio.sleep(1) # Esperar un segundo
    print("Tarea 2 finalizada")

async def tarea_paralelo():
    # Creamos dos tareas a partir de las funciones tarea_1() y tarea_2()
    _tarea_1 = asyncio.create_task(tarea_1())
    _tarea_2 = asyncio.create_task(tarea_2())

    # Ejecutar ambas tareas
    await asyncio.gather(_tarea_1, _tarea_2)

# Ejecutar la funcion tarea_paralelo
asyncio.run(tarea_paralelo())