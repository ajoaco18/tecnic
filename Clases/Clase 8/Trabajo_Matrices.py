import random
"""
Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).
Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
Menú:
Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). 
Si el chofer existe cargará la recaudación del viaje indicando línea y coche (no necesariamente un chofer está asignado a una única línea y coche), 
estos datos deben estar validados. Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches). 
Cada coche de cada línea puede tener varias recaudaciones diarias.

Mostrar la recaudación de cada coche y línea.
Calcular y mostrar recaudación por línea.
Calcular y mostrar recaudación por coche.
Calcular y mostrar la recaudación total.
Salir

Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, generación y verificación de existencia de legajo, cálculos, etc.
"""


lineas = 3
coches = 5
legajos_choferes = 15
legajos = [random.randint(1000, 9999) for i in range (legajos_choferes)]
matriz_legajos = [[0]* coches for i in range(lineas)] # crea matriz para almacenar legajos de choferes por linea y coche.
legajos_contador = 0
matriz_recaudaciones = [[0] * coches for i in range(lineas)]


for i in range(lineas):
    for j in range(coches):
        if legajos_contador < len(legajos): # comprueba si el contador es menor q la longitud de la lista, evita error cuando se llena la matriz.
            matriz_legajos[i][j] = legajos[legajos_contador] #asigna el legajo en la posicion correspondiente
            legajos_contador += 1

for i in range(lineas):
    for j in range(coches):
        print(matriz_legajos[i][j], end=" ")
    print()

def validar_legajo():
    ingreso_legajo = int(input("Ingrese su numero de legajo: "))
    for fila in matriz_legajos:
        if ingreso_legajo in fila:
            print("Legajo ingresado correctamente.")
            return True
    print("Error! Ingrese nuevamtne su legajo:")
    return False

def mostrar_matriz_recaudaciones():
    print("Matriz de recaudaciones:")
    for fila in matriz_recaudaciones:
        for valor in fila:
            print(valor, end=" ")
        print()

def ingresar_recaudacion():
    if validar_legajo():
        linea = int(input("Ingrese el numero de la linea (1, 2 o 3): ")) - 1 # Se le resta uno, asi agarra la pos 0
        coche = int(input("Ingrese el numero de coche(1 al 5): ")) - 1
        if 0 <= linea < lineas and 0 <= coche < coches:
            recaudacion = int(input("Ingrese la recaudacion del viaje: "))
            matriz_recaudaciones[linea][coche] += recaudacion # guarda la recaudacion en la pos correspondiente
            print("Recaudacion Registrada Correctamente.")
            mostrar_matriz_recaudaciones()
        else:
            print("Numero de coche o linea INCORRECTO.")
   

ingresar_recaudacion()







        



