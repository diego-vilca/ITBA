# import pandas as pd

# archivo = pd.read_excel('./Data/Datos.xlsx')
# # La variable archivo es de un tipo de dato especial de pandas llamado 'DataFrame'
# print(archivo)
##===================================================
#leo mi dataset
import pandas as pd
import os
from pprint import pprint
from libreria import wget


# llamo a la función y descargo el archivo excel de la web
# wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos.xlsx")


directorio = './Data'
archivo = 'Datos.xlsx'
fname = os.path.join(directorio, archivo)

# si agrego el parametro index_col puedo elegir con que columna quiero indexar
df = pd.read_excel(fname)

# Metodos y atributos de los DataFrame()
# muestro el dataframe
# print(df)
# muestro un indice con los nombres de las columnas
# print(df.columns)
# muestra el indice (rango numerico de lineas leidas del archivo)
# print(df.index)
# muestro las primeras n lineas de datos
# print(df.head(2))
# muestro las ultimas n lineas de datos
# print(df.tail(3))
# puedo chusmear datos numericos
# print(df[['Legajo', 'Quimica', 'Matematica', 'Fisica']].describe())

# Seleccion de datos
# muestro una columna (una serie)
# print(df['Nombre'])
# devuelvo una serie booleana (quienes cumplen o no con la condicion)
# print(df['Nombre'] == 'Sol')
# puedo sumar los True de esta serie para contar la cantidad de coincidencias
# print((df['Nombre'] == 'Sol').sum())
# devuelvo una serie con el numero de apariciones de cada elemento
# print((df['Nombre']).value_counts())

# creo una vista de df donde df_Sol es un dataframe con los alumnos llamados Sol y muestro solo las col Nombre y Apellido
# para poder modificarla sin tocar a df tengo que hacer una copia, asi que utilizo el metodo copy()
# df_Sol = df[df['Nombre'] == 'Sol'][['Nombre','Apellido','Matematica']].copy()
# print(df_Sol)
# accedo a la POSICION 1 de df_Sol
# print(df_Sol.iloc[1])
# accedo al INDICE 3 de df_Sol
# print(df_Sol.loc[3])
# También podemos acceder a rebanadas (slices) usando iloc
# Por ejemplo df_ejemplo.iloc[0:3]
# Por otra parte, podemos seleccionar tanto filas como columnas, si separamos con comas las respectivas selecciones:
# Este ejemplo nos devuelve las ultimas 5 filas y la tercer columna. Y siempre vienen acompañados del indice.
# df_ejemplo.iloc[-5:,2]

# muestro que modifique df_Sol y no toque df (aun no lo modifique)
# print(df[df['Nombre'] == 'Sol'][['Nombre','Apellido','Matematica']])

#ver como generar indices con fechas en git hub unsam

#=========================================================================================
# Manipulo los datos del archivo convirtiendolo en una estructura de datos nativa de python, en este caso un diccionario
# puedo convertir el dataframe en un diccionario con el metodo to_dict()
# recibe como parametro el tipo de diccionario de pandas
# tipos de diccionarios pandas: dict, list, series, split, records, index

# data = df.to_dict("list")
# # "list" significa que vamos a almacenar a cada columna como una lista con su contenido
# print(data)
# print(data['Nombre'][2])

# data1 = df.to_dict("records")
# Cada elemento de la lista es un diccionario que corresponde a cada una de las filas
# print(data1[2]['Nombre'])

# df_indexado = pd.read_excel(fname, index_col='Legajo')
# print(df)
# print(df_indexado)

#=========================================================================================


