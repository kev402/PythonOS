import subprocess as sp

def ejecutar_bat():
    ruta_bat = "C:/PythonOS/system/pysu.bat" 
    sp.run([ruta_bat], shell=True)