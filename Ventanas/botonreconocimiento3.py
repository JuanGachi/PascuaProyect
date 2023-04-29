import speech_recognition as sr
import webbrowser
import tkinter as tk
from googlesearch import search
from ttkthemes import ThemedTk
from tkinter import ttk



# Configuración del reconocimiento de voz
r = sr.Recognizer()
mic = sr.Microphone()

# Función para abrir la página web
def open_webpage(url):
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

# Función para reconocer la voz y abrir la página web
def recognize_webpage():
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            label.config(text="Di la página web que deseas abrir...")
            audio = r.listen(source)
        query = r.recognize_google(audio, language='es-ES')
        print("Has dicho: " + query)
        if "." not in query:
            query = query + ".com" 
        try:
            open_webpage("https://www." + query)
            label.config(text="Abriendo " + query)
        except:
            for url in search(query, stop=1):
                open_webpage(url)
            label.config(text="Buscando " + query)
    except sr.UnknownValueError:
        print("Lo siento, no he entendido lo que has dicho.")
        label.config(text="No te he entendido, por favor repite.")
    except sr.RequestError:
        print("Lo siento, ha ocurrido un error al procesar tu solicitud.")
        label.config(text="Ha ocurrido un error al procesar tu solicitud.")

# Configuración de la interfaz gráfica
root = ThemedTk(theme="equilux")
root.title("Reconocimiento de voz")
root.geometry("360x640")
root.resizable(False, False)

# Configuración del frame
frame = ttk.Frame(root, padding=(20, 50))
frame.place(relx=0.5, rely=0.5, anchor="center")

# Etiqueta para mostrar el mensaje
label = ttk.Label(frame, text="Di la página web que deseas abrir:", font=("Arial", 14))
label.pack(pady=20)

# Botón para reconocer la voz y abrir la página web
button = ttk.Button(frame, text="Reconocer voz", command=recognize_webpage)
button.pack(pady=20, ipadx=10, ipady=5)

root.mainloop()


