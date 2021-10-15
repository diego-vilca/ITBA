#%%
# palabra = input('Ingrese una palabra: ')
# intentos = 0

# while palabra != '':
#     letra = input()
    
#     if letra in palabra:
#         palabra = palabra.replace(letra, '')

#     intentos += 1
    

# print(intentos)

def ahorcado(palabra):
    intentos = 0

    while palabra != '':
        letra = input()
        
        if letra in palabra:
            palabra = palabra.replace(letra, '')

        intentos += 1

    return intentos


palabra = input()

print( ahorcado(palabra) )