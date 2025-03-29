import sys
import subprocess as sp
import psutil
import ctypes

def terminal():
    padre = psutil.Process().parent()  # Obtiene el proceso padre
    return padre.name() if padre else "Desconocido"

comando = sp.run(["pip", "list"], capture_output=True, text=True)
instalados = comando.stdout.splitlines()[2:]

ram_total = psutil.virtual_memory().total // (1024 ** 3)  # Convertir a GB
cpu_nucleos = psutil.cpu_count()
cpu_frecuencia = psutil.cpu_freq().max

# Obtener resolución de pantalla
user32 = ctypes.windll.user32
res_x = user32.GetSystemMetrics(0)
res_y = user32.GetSystemMetrics(1)

print(f"""
          .?77777777777777$.                       PythonOS - kev402
          777..777777777777$+                     --------------------------------
         .77    7777777777$$$                      OS: PythonOS (Windows)
         .777 .7777777777$$$$                      Kernel: Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}
         .7777777777777$$$$$$                      Packages: {len(instalados)} (pip)
         ..........:77$$$$$$$                      Terminal: {terminal()}
  .77777777777777777$$$$$$$$$.=======.             Total Memory: {ram_total} GB
 777777777777777777$$$$$$$$$$.========             CPU: {cpu_nucleos} núcleos, {cpu_frecuencia} MHz
7777777777777777$$$$$$$$$$$$$.=========            Resolution: {res_x}x{res_y}
77777777777777$$$$$$$$$$$$$$$.========= 
777777777777$$$$$$$$$$$$$$$$ :========+.
77777777777$$$$$$$$$$$$$$+..=========++~
777777777$$..~=====================+++++
77777777$~.~~~~=~=================+++++.
777777$$$.~~~===================+++++++.
77777$$$$.~~===============.d88888b.   .d8888b.  
 7$$$$$$$.================d88P" "Y88b d88P  Y88b  
 .,$$$$$$.================888     888 Y88b.     
         .=========~......888     888  "Y888b.    
         .=============+++888     888     "Y88b.
         .===========+++..888     888       "888
         .==========+++.  Y88b. .d88P Y88b  d88P
          ,=======++++++,,+"Y88888P"   "Y8888P" 
          ..=====+++++++++=.            
                ..~+=...     """)