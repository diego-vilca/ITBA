import pandas as pd
import os

data = {
    'Personas' : ['Analia Ferreyra', 'Martin Hugo', 'Fernando Lorenzo'],
    'Edad' : [25, 35, 87]
}

# creo el dataframe con mis datos
dataframe = pd.DataFrame(data)

print(dataframe)

# exporto el df
directorio = './Data'
archivo = 'Personas.xlsx'
dataframe.to_excel(os.path.join(directorio, archivo))

