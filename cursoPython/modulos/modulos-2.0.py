#Si el modulo estuviera en una carpeta de la misma ruta
#import funciones_buenas.saludar as m_saludar
import sys

sys.path.append("c:\\Users\\alanr\\OneDrive\\Desktop\\cursoPython\\funciones_buenas")

import saludar as modulo_saludo

print(modulo_saludo.saludar("Alan"))