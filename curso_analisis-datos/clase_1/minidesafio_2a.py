# Calcular el promedio de las notas de química de todos los alumnos en el archivo Datos.xlsx.

import pandas as pd
import os

directorio = './Data'
archivo = 'Datos.xlsx'
fname = os.path.join(directorio, archivo)

df = pd.read_excel(fname)
# print(df)

promedio = df['Quimica'].sum()/len(df['Quimica'])
print(f'Promedio notas de química: {promedio}')