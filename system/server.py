import subprocess as sp

def servidor():
    print("Crea servidores HTTP usando Python.")
    puerto = input("Ingresa el puerto donde correrá el servidor: ")
    try:
        proceso = sp.Popen(["python", "-m", "http.server", puerto])
        proceso.wait()  # Espera la interrupción manual
    except KeyboardInterrupt:
        print("\nServidor detenido.")
        proceso.terminate()