lista = [45, 9, 3, -3, 10, -2, 3]


################CALCULOS######################
suma = 0
for i in range(len(lista)):
    if lista[i] > 0:
        suma = suma + lista[i]



def sumar_positivos(lista: list) -> int |float|bool|None:
    """_summary_

    Args:
        lista (list): _description_

    Returns:
        int |[-2: no recibe una lista]|[-2: si la lista esta vacia]|[>=0: si pudo calcular]
    """
    retorno = -2
    if type(lista) == list:
        retorno = -1
        if len(lista) > 0:
            retorno = 0                    
            for i in range(len(lista)):       
                if lista[i] > 0:
                    retorno += lista[i]
    return retorno
lista = [44, -9, 77]
suma = sumar_positivos(lista)
if suma == -2:
    print("El valor ingresado no es lista.")
elif suma == -1:
    print("La lista esta vacia.")    
else:
    print(suma)
    

# print(f"La suma de los positivo es: {suma}")

############################################
################-MAXIMO-####################
bandera_maximo = True
for i in range(len(lista)):
    if bandera_maximo == True or  lista[i] > maximo_numero:
        maximo_numero = lista[i]
        bandera_maximo = False

print(f"El maximo es: {maximo_numero}")


def buscar_maximo(lista: list)-> int:
    bandera_maximo = True
    

# ############################################
# ################-Banderas-##################

bandera_negativo = False
for i in range (len(lista)):
    if lista[i] < 0:
        bandera_negativo = True
        break                            #Busca el primer numero negativo y rompe

if bandera_negativo == True:
    print("Por lo menos hay un numero negativo.")

else:
    print("No hay ningun numero negativo en la lista.")

def buscar_negativo(lista: list) -> int:
    
    
    
# ############################################
# lista = [45, 9, 3, -3, 10, -2, 3]
# numero_buscado = 3
# reemplazo = 1000
# for i in range(len(lista)):
#     if lista[i] == numero_buscado:
#         lista[i] = reemplazo                 #reemplaza la primer ocurrencia, q busco
#         break

# for i in range(len(lista)):
#     print(lista[i])
