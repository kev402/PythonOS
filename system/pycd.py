import os
from system import PATH

def cambiar_directorio():
    print("cd le permite cambiar de directorio.")
    ruta = input("Ingrese el nombre del directorio: ").strip()

    for wind, pyos in PATH.path.items():
        if ruta == pyos:  
            dir_actual = os.path.normpath(wind)  
            dir_actual = os.chdir(dir_actual)  
            return dir_actual

    print("Error: directorio no encontrado.")