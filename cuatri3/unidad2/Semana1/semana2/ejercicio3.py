import tkinter as tk

ventana = tk.Tk()
ventana.title("Formulario con grid")
ventana.geometry()
tk.Label(ventana, text="Usuario:").pack()
entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack()

tk.Label(ventana, text="Contraseña:").pack()
entrada_pass = tk.Entry(ventana, show="*")
entrada_pass.pack()
verificador=tk.Label(text="",fg="red", font=("arial",10))
verificador.place(x=60, y=90)
def comprobar():
    entrada=entrada_usuario.get()
    if entrada == "":
        verificador.config(text="ingresa texto")    

boton = tk.Button(ventana, text="Login", command=comprobar)
boton.place(x=16,y=90)

ventana.mainloop()