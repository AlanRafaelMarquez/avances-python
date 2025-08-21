#Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas_resueltos\\datos.csv")

#Convertir a string los datos de una columna
df["edad"] = df["edad"].astype(str)

#Mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df["edad"][0]))

#Remplazando los datos "Alan" por "Rafael"
df["apellido"].replace("Alan","Rafael",inplace=True)

#Eliminando las filas con datos vacios
df = df.dropna()

#Eliminando las filas repetidas
df = df.drop_duplicates()

#Creando un CSV con el dataframe resultante (Limpio)
df.to_csv("archivos_problemas_resueltos\\datos_limpios.csv")
print(df)
