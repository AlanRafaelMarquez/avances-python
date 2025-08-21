#Creamos un string
#s = "manipulación"

#Elimina cada segundo carácter del string
#print(s[::2])

#Te da el string en reversa     
#print(s[::-1])    

#1. Normalización de texto
#Eliminar acentos, convertir a minúsculas, y limpiar espacios
import unicodedata

def normalizar(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    return texto

print(normalizar("  Café con Leche  "))  # Output: 'cafe con leche'


#2. Tokenización personalizada
#Separar texto en palabras, ignorando puntuación
import re

texto = "¡Hola, mundo! ¿Cómo estás?"
tokens = re.findall(r'\b\w+\b', texto)
print(tokens)  # Output: ['Hola', 'mundo', 'Cómo', 'estás']

#3. Conteo de palabras únicas
#Usando Counter para frecuencia de palabras
from collections import Counter

texto = "Python es divertido. Python es poderoso."
palabras = re.findall(r'\w+', texto.lower())
frecuencia = Counter(palabras)
print(frecuencia)  # Output: {'python': 2, 'es': 2, 'divertido': 1, 'poderoso': 1}

#4. Extracción de datos estructurados
#Extraer fechas, correos, o números de un texto.
texto = "Mi cita es el 29/07/2025 y mi correo es alan.dev@example.com"
fechas = re.findall(r'\d{2}/\d{2}/\d{4}', texto)
correos = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', texto)
print(fechas)   # Output: ['29/07/2025']
print(correos)  # Output: ['alan.dev@example.com']

#5. Transformación condicional de strings
#Usar comprensión de listas para modificar palabras según reglas

frase = "Los datos son poder"
transformada = ' '.join([p.upper() if len(p) > 4 else p for p in frase.split()])
print(transformada)  # Output: 'Los DATOS SON PODER'

#6. Interpolación avanzada con f-strings
#Formateo dinámico con precisión y alineación

nombre = "Alan"
score = 95.6789
print(f"{nombre:>10} | {score:.2f}")  # Output: '      Alan | 95.68'

#7. Comparación de strings ignorando acentos y mayúsculas
#Ideal para búsquedas robustas.

def comparar(s1, s2):
    return normalizar(s1) == normalizar(s2)

print(comparar("Café", "cafe"))  # Output: True

#encontrar palabras palíndromas en un texto
texto = "anita laval la tina y Otto corre en radar"
palabras = re.findall(r'\b\w+\b', texto.lower())
palindromos = [p for p in palabras if p == p[::-1] and len(p) > 2]
print(palindromos)  # Output: ['anita', 'otto', 'radar']