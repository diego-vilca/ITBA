
numero = int(input('Ingrese un número: '))
pasos = 0

while numero > 1:
    if numero % 2 == 0:
        numero = numero / 2
            
    elif numero % 2 != 0:
        numero = numero * 3 + 1
            
    pasos += 1
    

print(pasos)

