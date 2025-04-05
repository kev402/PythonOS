from system import pycd
import shutil
import os


def rm():
    print("rm le permite borrar archivos y carpetas.")
    ruta = input("Ingrese la ruta del archivo o carpeta: ").strip()
    
    if ruta == "/" or ruta == "/system" or ruta == "/apps":
        print("No puedes borrar carpetas críticas")
    else:
        encontrado = False

        for real, emulado in pycd.PATH.path.items():
            # Verificar si la ruta ingresada comienza con la ruta emulada
            if ruta.startswith(emulado):
                # Eliminar la parte emulada y construir la ruta completa
                relativa = ruta[len(emulado):].lstrip("/")  # Quitar la parte emulada
                completa = os.path.join(real, relativa)  # Construir ruta real

                # Verificar si la ruta existe en el sistema
                if os.path.exists(completa):
                    try:
                    # Verificar si es un directorio para eliminar recursivamente
                        if os.path.isdir(completa):
                            shutil.rmtree(completa)
                            print(f"Carpeta eliminada exitosamente: {completa}")
                        else:
                            os.remove(completa)
                            print(f"Archivo eliminado exitosamente: {completa}")
                        encontrado = True
                        break
                    except PermissionError:
                        print(f"Error: No tiene permisos para borrar: {completa}.")
                    except Exception as e:
                        print(f"Error inesperado al intentar borrar {completa}: {e}")

        if not encontrado:
            print("Error: No se pudo localizar el archivo o carpeta especificado dentro de las rutas configuradas.")
