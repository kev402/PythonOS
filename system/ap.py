import subprocess as sp 

def actualizar(paquete):
    sp.run(["pip", "install", "--upgrade", paquete])

def ap():
    print("Bienvenido a AP - AutoPip, ayudamos a instalar tus módulos de pip en PythonOS para todo tu Windows.")
    print("""MENÚ DE OPCIONES:
1. Instalar paquete.
2. Desinstalar paquete.
3. Listar paquetes.
4. Comprobar dependencias rotas.
5. Actualizar pip.
6. Limpiar caché.
7. Actualizar paquete.
""")
    comando = int(input("Ingresa la opción que deseas usar: "))
    if comando == 1 or comando == 2 or comando == 7:
        paquete = input("Ingresa nombre del paquete: ")
        if comando == 1:
            sp.run(["pip", "install", paquete])
        elif comando == 2:
            sp.run(["pip", "uninstall", paquete])
        else:
            actualizar(paquete)
    elif comando == 3:
        sp.run(["pip", "list"])
    elif comando == 4:
        sp.run(["pip", "check"])
    elif comando == 5:
        actualizar("pip")
    elif comando == 6:
        sp.run(["pip", "cache", "purge"])
    else:
        print("Orden incorrecta, intente otra vez.")