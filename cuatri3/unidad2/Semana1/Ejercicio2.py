import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera app")
ventana.geometry("400x200")

etiqueta = tk.Label(ventana, text="¡Hola, mundo!", fg="red")
etiqueta2 = tk.Label(ventana, text="Aprendiendo GUI con tinker")

etiqueta.pack()
etiqueta2.pack()

def saludar():
    etiqueta.config(text="¡Hola desde Tkinter!")

def adios():
    etiqueta.config(text="¡Adios!")
    
boton = tk.Button(ventana, text="Presioname", command=saludar)
boton2 = tk.Button(ventana, text="Despideme", command=adios)


boton.pack()
boton2.pack()

ventana.mainloop()