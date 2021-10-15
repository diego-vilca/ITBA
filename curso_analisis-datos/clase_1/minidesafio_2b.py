# Escribir una funcion que reciba como parámetros: una variable de tipo DataFrame (la tabla de alumnos) y el índice de un alumno. 
# Luego debe devolver con return el promedio de sus notas en las diferentes materias.

import pandas as pd
import os

def promedio_notas(dataframe, indice):
    '''Recibe un dataframe y el indice del alumno, y retorna el promedio de notas
    '''
    alumno = dataframe.loc[indice]
    promedio = (alumno['Quimica'] + alumno['Matematica'] + alumno['Fisica'])/3
    return promedio


def f_principal(argv):
    if len(argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'un_indice')
    
    directorio = './Data'
    archivo = 'Datos.xlsx'
    fname = os.path.join(directorio, archivo)
    df = pd.read_excel(fname)
    indice = int(argv[1])
    # print(df)
    print(f'El promedio de notas es: {promedio_notas(df, indice)}')


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)

# df = pd.read_excel(fname)
# print(df)
# print(df.loc[0]['Quimica'])