import shutil
import os
from system import pycd

def translate_path(ruta_emulada):
    """Convierte una ruta emulada en su equivalente real, asegurando la barra."""
    for wind, pyos in pycd.PATH.path.items():
        if ruta_emulada.startswith(pyos):  # Verifica si la ruta comienza con el alias
            sub_ruta = ruta_emulada[len(pyos):].lstrip("/")  # Extrae el resto de la ruta
            return os.path.join(wind, sub_ruta)  # Une correctamente con la raíz real
    return None

def copiar(origen, destino):
    """Copia un archivo/directorio de una ruta emulada a otra."""
    origen_real = translate_path(origen)
    destino_real = translate_path(destino)

    if not origen_real or not destino_real:
        print("Error: ruta inválida.")
        return

    try:
        # Si el origen es un archivo, asegurarse de que la carpeta destino existe
        if os.path.isfile(origen_real):
            destino_folder = os.path.dirname(destino_real)
            if not os.path.exists(destino_folder):
                os.makedirs(destino_folder)  # Crea los directorios faltantes
            shutil.copy2(origen_real, destino_real)
        
        # Si el origen es una carpeta, asegurarse de que la carpeta padre existe
        elif os.path.isdir(origen_real):
            if not os.path.exists(destino_real):
                os.makedirs(destino_real)  # Crea la carpeta destino
            shutil.copytree(origen_real, destino_real, dirs_exist_ok=True)

        print(f"Copiado correctamente de {origen} a {destino}.")
    except Exception as e:
        print(f"Error al copiar: {e}")

def mover(origen, destino):
    origen_real = translate_path(origen)
    destino_real = translate_path(destino)

    if not origen_real or not destino_real:
        print("Error: ruta inválida.")
        return

    # 🔹 VERIFICACIÓN ADICIONAL
    if not os.path.exists(origen_real):
        print(f"[ERROR] El archivo NO existe: {origen_real}")
        return
    if not os.path.exists(os.path.dirname(destino_real)):
        print(f"[ADVERTENCIA] Creando directorio: {os.path.dirname(destino_real)}")
        os.makedirs(os.path.dirname(destino_real), exist_ok=True)

    try:
        shutil.move(origen_real, destino_real)
        print(f"Movido correctamente de {origen} a {destino}.")
    except Exception as e:
        print(f"Error al mover: {e}")

def interfaz():
    print("Bienvenido a portfile, aquí podrás mover y copiar archivos y carpetas de una ruta a otra.")
    pregunta = input("mover o copiar?: ").strip().lower()
    ruta_origen = input("Ingresa la ruta origen: ")
    ruta_destino = input("Ingresa la ruta destino: ")
    if pregunta == "mover":
        mover(ruta_origen, ruta_destino)
    elif pregunta == "copiar":
        copiar(ruta_origen, ruta_destino)
    else:
        print("Ingrese lo que quiere hacer correctamente.")
