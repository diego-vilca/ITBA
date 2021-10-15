# Obtener el promedio general sólo para aquellos alumnos que aprobaron Matemática en el archivo Datos.xlsx.

import pandas as pd
import os
from minidesafio_2b import promedio_notas

directorio = './Data'
archivo = 'Datos.xlsx'
fname = os.path.join(directorio, archivo)

df = pd.read_excel(fname)
aprobados_mate = df[df['Matematica'] >= 6] 
# print(aprobados_mate)
for indice in aprobados_mate.to_dict('index'):
    nombre = aprobados_mate["Nombre"][indice]
    apellido = aprobados_mate["Apellido"][indice]
    print(f'Promedio de {apellido} {nombre}: {promedio_notas(aprobados_mate, indice)} ')
