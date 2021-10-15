# Armar una función que copie un archivo .xlsx, y lo guarde como "Copia 1 -  nombre ", de ya existir debe guardarlo como Copia 2 -, Copia 3 - , ...

import os
import shutil

def copiadora(archivo):
    '''recibe el nombre de un archivo.xlsx ubicado el el directorio actual, y lo copia a la carpeta Data
    '''
    # evaluo que sea un archivo .xlsx
    archivo_spliteado = os.path.splitext(archivo)

    if archivo_spliteado[1] != '.xlsx':
        print('Extension invalida, el archivo debe ser .xlsx')
        
    else:
        version = 1

        while os.path.exists("./Data/Copia "+ str(version) + " "+ archivo):
            version += 1

        path_destino = "./Data/Copia "+ str(version) + " "+ archivo

        shutil.copyfile(archivo, path_destino)

# copiadora('test.xls')

