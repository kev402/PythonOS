import customtkinter as ctk
import webview

def abrir_web():
    url = entrada.get()
    ventana.destroy()
    webview.create_window("WebCenter", url)
    webview.start()

def crear_web(nombre, url):
    ventana.destroy()
    webview.create_window(nombre, url)
    webview.start()

def ia():
    crear_web("ChatGPT", "https://chatgpt.com")

def google():
    crear_web("Google", "https://google.com")

def youtube():
    crear_web("YouTube", "https://youtube.com")

def github():
    crear_web("GitHub", "https://github.com")

ventana = ctk.CTk()
ventana.title("WebCenter")
ventana.geometry("450x320")

texto = ctk.CTkLabel(ventana, text="WebCenter le permite ver sitios como apps nativas. Ingrese la url:")
texto.pack()
entrada = ctk.CTkEntry(ventana)
entrada.pack(pady=10)

boton = ctk.CTkButton(ventana, text="Ir a url", command=abrir_web)
boton.pack()

texto2 = ctk.CTkLabel(ventana, text="Atajos rápidos con apps populares:")
texto2.pack(pady=5)

boton2 = ctk.CTkButton(ventana, text="Google", command=google)
boton2.pack(pady=5)

boton3 = ctk.CTkButton(ventana, text="ChatGPT", command=ia)
boton3.pack(pady=5)

boton4 = ctk.CTkButton(ventana, text="YouTube", command=youtube)
boton4.pack(pady=5)

boton5 = ctk.CTkButton(ventana, text="GitHub", command=github)
boton5.pack(pady=5)

ventana.mainloop()