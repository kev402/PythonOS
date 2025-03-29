import os
import json

RUTA = "C:/PythonOS/apps/"

# Cargar patrones de advertencia desde un archivo JSON
try:
    with open("C:/PythonOS/system/patrones.json", "r", encoding="utf-8") as f:
        PATRONES = json.load(f)
except FileNotFoundError:
    print("Error: No se encontró el archivo 'patrones.json'.")
    exit(1)

def buscar_archivos(ruta):
    archivos = []
    for root, _, files in os.walk(ruta):
        for file in files:
            if file.endswith(".py"):
                archivos.append(os.path.join(root, file))
    return archivos

def analizar_archivo(archivo):
    try:
        with open(archivo, "r", encoding="utf-8", errors="ignore") as f:
            contenido = f.read()
    except Exception as e:
        print(f"No se pudo leer {archivo}: {e}")
        return []
    
    reportes = []
    for patron, mensaje in PATRONES.items():
        if patron in contenido:
            alerta = f"⚠️ {archivo}: {mensaje}"
            reportes.append(alerta)
            print(alerta)

    return reportes

def escanear():
    print("VulnCode escanea únicamente archivos .py en la carpeta /apps y subcarpetas.")
    archivos = buscar_archivos(RUTA)
    if not archivos:
        print("No se encontraron archivos .py en la carpeta.")
        return

    print(f"Escaneando {len(archivos)} archivos en {RUTA}...\n")

    reportes = []
    for archivo in archivos:
        reportes += analizar_archivo(archivo)

    with open("reporte.txt", "w", encoding="utf-8") as f:
        for linea in reportes:
            f.write(linea + "\n")

    print("\nAnálisis completado. Revisa el archivo 'reporte.txt'.")
