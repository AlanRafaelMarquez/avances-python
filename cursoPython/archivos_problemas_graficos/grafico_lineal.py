import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\jugue2.csv")

#Creando el grafico
sns.lineplot(x="fecha",y="jugue",data=df)

#Creando un punto del momento que mas jugue
plt.plot("01-09",17,"o")

#Mostrando el grafico
plt.show()