conjunto = {"Alan","Hombre",18}

agregar_elementos = conjunto.add("Rafael")
agregar_varios_elementos = conjunto.update(["Aguascalientes","Programador"])

eliminar_con_remove = conjunto.remove("Alan")
eliminar_con_discard = conjunto.discard(18)

elemento_aleatorio = conjunto.pop()


print(conjunto)