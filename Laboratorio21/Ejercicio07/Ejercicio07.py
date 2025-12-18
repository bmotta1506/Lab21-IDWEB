import os

def copiar_archivo_texto(origen, destino):
    try:
        with open(origen, 'r', encoding='utf-8') as f_origen:
            contenido = f_origen.read()
            with open(destino, 'w', encoding='utf-8') as f_destino:
                f_destino.write(contenido)
        print(f"Texto copiado con éxito de {origen} a {destino}")
    except FileNotFoundError:
        print("Error: El archivo de texto de origen no existe.")

def copiar_archivo_binario(origen, destino):
    try:

        with open(origen, 'rb') as f_origen:
            contenido = f_origen.read()
            with open(destino, 'wb') as f_destino:
                f_destino.write(contenido)
        print(f"Archivo binario copiado con éxito ({origen} -> {destino})")
    except FileNotFoundError:
        print("Error: El archivo binario de origen no existe.")

copiar_archivo_texto('notas.txt', 'notas_copia.txt')

copiar_archivo_binario('foto.jpg', 'foto_copia.jpg')