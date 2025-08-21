diccionario = {
    "Nombre": "Alan",
    "Apellido": "Marquez",
    "Edad" : 18
}

#Recorriendo diccionario con items() para obtener las claves y los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es : {key} y el valor es : {value}")
    