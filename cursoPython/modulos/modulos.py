#Importando un modulo y asignadole el nombre "m_saludar"
#Import modulo_saludar as m_saludar

#Desde ese modulo, importamos dos funciones y les cambiamos los nombres
from modulo_saludar import saludar as saludar_normal,saludar_raro as saludar_como_cosu
import modulo_saludar as m_saludar

#Creamos las variables con los saludos
saludo = saludar_normal("Alan")
saludo_raro = saludar_como_cosu("Rafael")

#Mostramos los resultados
print(saludo)  
print(saludo_raro)

#Para ver todas las propiedades y metodos del el namespace
#print(dir(m_saludar))

#Accedemos al nombre del modulo
print(__name__)

#Accedemos al nombre del modulo llamado
#print(m_saludar.__name__)