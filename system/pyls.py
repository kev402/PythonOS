import os

def listar_archivos():
    for item in os.scandir("."):
        tipo= "[DIR]" if item.is_dir() else "[FILE]"
        print(f"{tipo}: {item.name}")