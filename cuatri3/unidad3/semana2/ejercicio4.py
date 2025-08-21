#
agenda = {
    "Alan":444,
    "Alejandro":555,
    "Carlos":666
}

pedir = input("Dime algun nombres entre Alan, Alejandro y Carlos y te digo su numero: ")

print(agenda.get(pedir, "No se encuentra"))

