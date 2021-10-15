# Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato y determinar qué equipo es el campeón (1ro)
#  y perdedor (último). El archivo tiene cuatro columnas, Equipo, Puntos, Goles a favor y Goles en contra.

import pandas as pd
import os

directorio = './Data'
archivo = 'Tabla1.xlsx'
fname = os.path.join(directorio, archivo)

df = pd.read_excel(fname)
# df_dict = df.copy()
df_dict = df.copy().to_dict('list')

print(df)
# print(df_dict)
index_ganador = df_dict["Puntos"].index(max(df_dict["Puntos"]))
index_ultimo = df_dict["Puntos"].index(min(df_dict["Puntos"]))

print(f'El ganador es el {df_dict["Equipo"][index_ganador]}')
print(f'El último es el {df_dict["Equipo"][index_ultimo]}')