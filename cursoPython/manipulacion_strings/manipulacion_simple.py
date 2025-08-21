#1. Eliminar espacios extra
texto = "   Hola   mundo   "
limpio = ' '.join(texto.split())
print(limpio)  # Output: 'Hola mundo'


#Útil para limpiar texto antes de procesarlo.


#2. Buscar una palabra dentro de un texto
texto = "Python es divertido"
print("divertido" in texto)  # Output: True


#Ideal para filtros o validaciones simples.


#3. Reemplazar múltiples palabras
texto = "Hola mundo cruel"
texto = texto.replace("cruel", "hermoso").replace("Hola", "Hey")
print(texto)  # Output: 'Hey mundo hermoso'


# Encadenar .replace() es una forma poderosa y sencilla.


#4. Unir palabras con un separador
palabras = ["Python", "es", "genial"]
frase = ' '.join(palabras)
print(frase)  # Output: 'Python es genial'


#Muy útil para construir frases dinámicas.


#5. Extraer solo letras o números
import re

texto = "Código 123 listo!"
solo_letras = re.sub(r'[^a-zA-Z ]', '', texto)
solo_numeros = re.sub(r'\D', '', texto)
print(solo_letras)   # Output: 'Código  listo'
print(solo_numeros)  # Output: '123'


#Primer paso hacia expresiones regulares.


#6. Contar cuántas veces aparece una palabra
texto = "Python es divertido. Python es poderoso."
conteo = texto.lower().count("python")
print(conteo)  # Output: 2


#Útil para análisis de frecuencia.



