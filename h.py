import tkinter as tk
import random

# Lista de palabras
words = ["noob", "guest", "alien", "zombie", "vampire", "admin", "warrior", "wizard", "gnome", "blocker", "ROBLOX", "Classic"]

# Función que genera una palabra aleatoria
def generate_word():
    random_word = random.choice(words)
    word_label.config(text=random_word)

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Palabras")

# Establecer el tamaño de la ventana
root.geometry("300x200")

# Crear un Label para mostrar la palabra generada
word_label = tk.Label(root, text="Haz clic para generar una palabra", font=("Arial", 14))
word_label.pack(pady=20)

# Crear un botón para generar una palabra
generate_button = tk.Button(root, text="Generar Palabra", font=("Arial", 12), command=ge…
