import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw() # Oculta la ventana default

nombre = simpledialog.askstring("Nombre", "Introduce el nombre del alumno")
calificaciones = []

for i in range(3) :
    calificacion = float(simpledialog.askfloat("Nombre", f"Introduce la calificación del parcial {i + 1}"))
    calificaciones.append(calificacion)

promedio = sum(calificaciones) / len(calificaciones)

messagebox.showinfo("Resultado", f"El promedio de {nombre} es: {promedio}")