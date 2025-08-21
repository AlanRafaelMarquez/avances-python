import tkinter as tk
ventana = tk.Tk()
ventana.title("Mi app")
ventana.geometry("300x150")

etiqueta = tk.Label(ventana, text="¡Hola,mundo!")
etiqueta.pack()
def saludar(): 
    etiqueta.config(text="¡Hola desde Tkinter!")
boton = tk.Button(ventana, text="Saludar",command=saludar()) 
boton.pack()
ventana.mainloop()


