import os
from system import portfile

def cat():
    print("cat le permite leer textos en consola.")
    ruta_emulada = input("Ingrese la ruta del archivo: ").strip()
    
    ruta_completa = portfile.translate_path(ruta_emulada)
    
    if ruta_completa is None:
        print(f"Error: La ruta '{ruta_emulada}' no existe en el sistema.")
        return

    ruta_completa = os.path.normpath(ruta_completa)

    try:
        with open(ruta_completa, 'rb') as archivo:
            contenido = archivo.read()
            try:
                print(contenido.decode())  # Intenta decodificar como texto
            except UnicodeDecodeError:
                print("Error: El archivo no es de texto y no se puede mostrar.")
    except PermissionError:
        print(f"Error: No tiene permisos para leer el archivo ({ruta_completa}).")
    except Exception as e:
        print(f"Error inesperado: {e}")
