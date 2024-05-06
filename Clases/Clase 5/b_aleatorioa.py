mi_lista = [-1] * 5
bandera_salida = True

while bandera_salida == True:
    index = int(input("Ingrese la posicion: "))
    while index < 1 or index > len(mi_lista):
        index = int(input("Reingrese la posicion: "))
    numero = int(input("Ingrese un numero: "))
    
    mi_lista[index] = numero
    
    seguir = input("Continua? si/no")
    if seguir == "no":
        break

    for i in range(len(mi_lista)):
        if mi_lista[i] != -1:
            print(f"{i+1} -- {mi_lista[i]}")
