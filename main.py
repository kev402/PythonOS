'''PythonOS - bajo la licencia AGPLv3 - por kev402 en https://github.com/kev402/ y https://gitlab.com/kev402/
Versión únicamente usable en Windows, la versión Linux estará disponible pronto.
Para entender la licencia AGPLv3, visite https://www.gnu.org/licenses/agpl.html o vea el archivo LICENSE.
Si necesita documentación vaya a https://kev402.github.io/PythonOS/
'''

from system import pyls, ap, boot, pycd, pycat, server, pyrm, help, portfile, pysu, scan # importamos las apps del sistema
import subprocess as sp 
import os

boot.boot() # arrancamos el sistema verificando dependencias

while True:

    dir_actual = os.getcwd()

    pyos_dir = None
    for ubicacion, ubic in pycd.PATH.path.items():
        if dir_actual in ubicacion:
            pyos_dir = ubic
            break
    if pyos_dir is None:
        print("Error: directorio no encontrado.")

    comandos = {
        "cd": pycd.cambiar_directorio,
        "ls": pyls.listar_archivos,
        "ap": ap.ap,
        "cat": pycat.cat,
        "server": server.servidor,
        "rm": pyrm.rm,
        "help": help.mensaje,
        "portfile": portfile.interfaz,
        "su": pysu.ejecutar_bat,
        "vulncode": scan.escanear
    }

    comando = input((f"""┌──[{pyos_dir}]
└─$ """))  # Banner con ruta actual para el usuario

    for com, func in comandos.items():
        if comando.strip().lower() == com:
            func() # busca posibles entradas coincidentes en el diccionario comandos
            break # rompe cuando encuentre una coincidencia
    if comando.strip() == "python":
        sp.run(["python"]) # inicia python del sistema
    elif comando.strip() == "shutdown":
        print("PythonOS está siendo apagado...")
        break
    elif all(comando.strip().lower() != c for c in comandos):
        sp.run(["python", f"C:/PythonOS/apps/{comando}.py"]) # si no coincide ningún comando se intenta ejecutar como una app