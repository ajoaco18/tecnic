def num_positivo_negativo(lista: list):
    positivos = 0 
    negativos = 0
    for i in lista:
        if i > 0:
            positivos += 1 # Agrega +1 en positivos, cada vez que encuentra un positivo
        else:
            negativos += 1 # Lo mismo pero en negativo,
    return positivos, negativos
# lista = [4, -6, 14, -2]
# total_positivos, total_negativos = num_positivo_negativo(lista)
# print(f"Total positivos: {total_positivos}, Total negativos {total_negativos}")

def suma_pares(lista: list):
    suma = 0
    for i in lista:
        if i % 2 == 0:
            suma += i # Se va sumando cada numero par que encuentra.
    return suma
# lista = [3, 6, 9, 12, 15, 18]
# total_suma = suma_pares(lista)
# print(f"La sumatoria de los numeros pares es: {total_suma}")


