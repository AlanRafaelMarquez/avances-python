import pandas as pd
#Usando la funcion de read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#Obteniendo los datos de la culumna nombre
nombres = df["nombre"]

#Ordenar con dataframe por edad
df_ordenado_asendente = df.sort_values("edad")

#Ordenando de forma decendente
df_ordenado_desendente = df.sort_values("edad",ascending=False)

#Concatenando con los dos dataframe
df_concatenado = pd.concat([df,df2])

#Accediendo a las primeras 3 filas con head()
primeras_fila = df.head(2)

#Accediendo a las 2 ultimad filas con tail()
ultimas_filas = df.tail(2)

#Accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#Obteniedo data estadistica del dataframe
df_info = df.describe()

#Accediendo a la edad de la fila 2
elemento_especifico = df.loc[2,"edad"]

#Accediendo a la edad de la fila 2 con iloc
elemento_especifico = df.iloc[2,2]

#Accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#Accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#Accediendo a las filas con edad mayor a 30
mayor_a_30 = df.loc[df["edad"]<30,:]
print(mayor_a_30)