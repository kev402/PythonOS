from importlib.util import find_spec
import subprocess as sp
import shutil
import time
import os

def instalado(paquete):
    nombre_modulo = "webview" if paquete == "pywebview" else paquete
    return find_spec(nombre_modulo) is not None

def verificar(paquete):
    print(f"Verificando existencia de {paquete}...")
    if instalado(paquete):
        print(f"{paquete} está instalado...")
    else:
        print(f"Advertencia {paquete} no está instalado, {paquete} es una dependencia importante para el funcionamiento de PythonOS.")
        print(f"Intentando instalar {paquete}...")
        time.sleep(5)
        sp.run(["pip", "install", f"{paquete}"], check=True)
        print(f"Instalado correctamente...")

def boot():
    print("Bienvenido a PythonOS, ingrese help para obtener mas información.")
    time.sleep(3)
    print("Verificando dependencias...")
    print("Verificando existencia de pip...")
    if  shutil.which("pip"):
        print("pip está instalado...")
    else:
        print("Advertencia pip no está instalado, pip es una dependencia importante para el funcionamiento de PythonOS.")
        print("Intentando instalar pip...")
        time.sleep(5)
        sp.run(["curl", "-o", "script.py", "https://bootstrap.pypa.io/get-pip.py"], check=True)
        print("Descargado, intentando instalar...")
        time.sleep(3)
        sp.run(["python", "script.py"], check=True)
        os.remove("script.py")
        print("Instalado correctamente...")
    verificar("psutil")
    verificar("pywebview")
    verificar("customtkinter")
