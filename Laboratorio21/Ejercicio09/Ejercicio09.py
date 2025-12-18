import time
import random
import threading
import asyncio
import multiprocessing

def consulta_bd(id_consulta):
    tiempo = random.randint(1, 5)
    print(f"Consulta {id_consulta} iniciando (tardará {tiempo}s)...")
    time.sleep(tiempo)
    print(f"Consulta {id_consulta} finalizada.")
    return tiempo

def ejecutar_hilos():
    hilos = []
    for i in range(3):
        h = threading.Thread(target=consulta_bd, args=(i+1,))
        hilos.append(h)
        h.start()
    for h in hilos:
        h.join()

async def consulta_async(id_consulta):
    tiempo = random.randint(1, 5)
    print(f"Consulta {id_consulta} (Async) iniciando (tardará {tiempo}s)...")
    await asyncio.sleep(tiempo) 
    print(f"Consulta {id_consulta} (Async) finalizada.")

async def ejecutar_async():
    tareas = [consulta_async(i+1) for i in range(3)]
    await asyncio.gather(*tareas)

def ejecutar_procesos():
    procesos = []
    for i in range(3):
        p = multiprocessing.Process(target=consulta_bd, args=(i+1,))
        procesos.append(p)
        p.start()
    for p in procesos:
        p.join()

if __name__ == "__main__":
    print("--- INICIANDO PRUEBA DE CONCURRENCIA ---\n")
    
    start = time.time()
    print("MÉTODO: HILOS")
    ejecutar_hilos()
    print(f"Tiempo Total Hilos: {time.time() - start:.2f}s\n")

    start = time.time()
    print("MÉTODO: ASINCRONÍA")
    asyncio.run(ejecutar_async())
    print(f"Tiempo Total Async: {time.time() - start:.2f}s\n")

    start = time.time()
    print("MÉTODO: PROCESOS")
    ejecutar_procesos()
    print(f"Tiempo Total Procesos: {time.time() - start:.2f}s")