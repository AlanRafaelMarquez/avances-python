import tkinter as tk
ventana = tk.Tk()
ventana.title("Entrada")
ventana.geometry("300x300")

etiqueta1 = tk.Label(ventana, text="Dame tu nombre: ")
etiqueta1.pack()
nombre = tk.Entry(ventana)

nombre.pack()
etiqueta2 = tk.Label(ventana, text="Dame tus apellidos: ")
etiqueta2.pack()
apellido = tk.Entry(ventana)
apellido.pack()

def resultado():
    nombre2 = nombre.get()
    etiqueta1.config(text=f"Hola  {nombre2}".upper())
    apellido1 = apellido.get()
    etiqueta2.config(text=f"{apellido1}")

def letras():
    nombre4 = nombre.get()
    cantidad_letras = len(nombre4)
    label_resultado.config(text=f"Cantidad de letras: {cantidad_letras}")

boton_contar = tk.Button(ventana, text="Contar letras", command=letras)
boton_contar.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

boton = tk.Button(ventana, text="Mostrar", command=resultado, )
boton.pack()

ventana.mainloop()