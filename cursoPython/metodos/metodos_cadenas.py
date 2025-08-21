cadena1 = "hola,soy,alan"
cadena2 = "Bienvenido maquina"

#print(dir(cadena1))

#convierte a mayusculas
mayus = cadena1.upper()

#Convierte a minusculas
minus = cadena1.lower()

#Primera letra en mayuscula
primera_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay condiciones devuelve -1
busqueda_find = cadena1.find("a")

#Buscamos una cadena en otra cadena, si hay coincidencias lanza una exepcion
busqueda_index = cadena1.index("a")

#Si es numerico devuelve True, si no devolvemos False
es_numerico = cadena1.isnumeric()

#Si es alfa numerico devolvemos True, si no devolvemos False
es_alfanumerico = cadena1.isalpha()

#Buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("a")

#Contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#Verificamos si una cadena empieza con otra cadena, si es asi devuelve True
empieza_con = cadena1.startswith("hola")

#Verificamos si una cadena termina con otra cadena, si es asi devuelve True
termina_con = cadena1.endswith("an")

#remplaza un pedazo de la cadena, por otra cadena
cadena_nueva = cadena1.replace("alan","rafael")
cadena_nueva2 = cadena_nueva.capitalize()

#Separa cadenas con la cadena que le pasamos
cadena_separada = cadena1.split(",")
print(cadena_separada)