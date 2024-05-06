
def num_positivo_negativo(lista: list):
    positivos = 0
    negativos = 0
    for i in lista:
        if i > 0:
            positivos += 1
        elif i < 0:
            negativos += 1
    return positivos, negativos

# lista = [4, -6, 14, -2]

# total_positivos, total_negativos = num_positivo_negativo(lista)


# print(f"Cantidad de numeros positivos {total_positivos}, Cantidad de numeros negativos: {total_negativos}")



def sumatoria_pares(lista: list):
    suma = 0
    for i in lista:
        if i % 2 == 0:
            suma += i
    return suma
    

# lista = [3, 6, 9, 12, 15, 18]
# resultado = sumatoria_pares(lista)
# print(f"La sumatoria de los numeros pares es: {resultado}")

def max_impares(lista: list): 
    bandera_max_impar = True
  
    for i in lista:
        if i % 2 != 0:
            if bandera_max_impar == True:
                numero_maximo = i
                bandera_max_impar = False
            elif numero_maximo < i:
                numero_maximo = i
            

    return numero_maximo
# lista = [3, 6, 9, 12, 15, 18]
# resultado = sumatoria_impares(lista)
# print(f"La sumatoria de los numeros impares de la lista es: {resultado}")

def numeros_listas(lista: list):
    for i in lista:
        print(lista)

# lista = [3, 6, 9, 12, 15, 18]
# print(f"Lista de numeros ingresados: {lista}")

def todos_num_pares(lista: list):
    for i in lista:
        if i % 2 == 0:
            print(i)

# lista = [3, 6, 9, 12, 15, 18]
# lista_num_pares = todos_num_pares(lista)
# print(f"Lista de todos los numeros pares: {lista_num_pares}")

def posiciones_impares(lista: list):
    for i in range(len(lista)): #Muestra indice y valor ingresado
        if i % 2 != 0:
            numero = lista[i]
            print(f"Posicion: {i}, Numero: {numero}")

# lista = [3, 6, 9, 12, 15, 18]
# posiciones_impares(lista)




















    