import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\confla_ingresos.csv")

#Creando el grafico
sns.barplot(x="fuente",y="ingreso",data=df)

#Obteniendo el total de ingresos
total_ingresos = df["ingreso"].sum()

#Mostrando el total
print(f"El total de ingresos es: ${total_ingresos} USD")

#Mostrando el grafico
plt.show()