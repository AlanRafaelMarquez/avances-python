import tkinter as tk

ventana = tk.Tk()
ventana.title("Botones y Etiquetas")
ventana.geometry("1900x1000")

etiqueta = tk.Label(ventana, text="Esperando...")
etiqueta.pack()

etiqueta2 = tk.Label(ventana, text="Hola", font=("Helvetica", 14, "bold italic"))
etiqueta2.pack()

def actualizar():
    etiqueta.config(text="¡Botón presionado!",  fg="red", font=("Helvetica", 14, "bold italic"))
    etiqueta2.config(text="¡Adios!",  fg="green", font=("Comic Sans MS", 20))
    boton.config(text="¡negro!",  fg="black", font=("Helvetica", 16, "bold"))


boton = tk.Button(ventana, bg="blue", text="Presióname",  fg="red",  command=actualizar)
boton.pack()
ventana.mainloop()