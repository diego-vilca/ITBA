# Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato. El archivo tiene cuatro columnas, Equipo, Puntos, Goles a favor y Goles en contra. 
# Determinar de cada equipo la diferencia de gol (goles a favor - goles en contra), y mostrar todas las diferencias de gol usando print.

from libreria import wget
import pandas as pd
import os

# descargo el archivo tabla en mi carpeta data
# wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Tabla1.xlsx")

directorio = './Data'
archivo = 'tabla1.xlsx'
fname = os.path.join(directorio, archivo)

# leo el dataframe
df = pd.read_excel(fname, index_col= 'Equipo')
# print(df)

df.to_dict('list')
serie_diferencia = df['Goles a favor'] - df['Goles en contra']
print(serie_diferencia)
# print(type(serie_diferencia))
# print(type(df))