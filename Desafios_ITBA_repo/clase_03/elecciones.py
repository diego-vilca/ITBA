
votos_totales = int(input())
d = {}

for i in range(0, votos_totales):
    votado = input()
    
    # .get( clave, valor_por_defecto ): Devuelve el valor asociado a la clave. Si la clave no se encuentra el diccionario, 
    # devuelve el valor por defecto indicado. Esto es útil cuando no sabemos si una clave existe o no.
    d[votado] = d.get(votado, 0) + 1

# El primer parametro de max() es mi iterable (d), get() retorna el valor de la clave
# Le asigno a la palabra reservada key el criterio para su funcionamiento, en este caso que tenga en cuenta los values
# la funcion get() va sin parentesis porque no la estoy llamando
print(max(d, key = d.get))

    


