
from os import system
bandera_seguir = True
bandera_numeros_ingresados = False

while bandera_seguir:
    opcion = int(input("1. Ingresar datosn2.Sumarn3.Restarn4Multiplicarn5.Dividirn6.SalirnElija Una opcion: "))
    match opcion:
        case 1:
         numero_1 = int(input("ingrese el primer numero"))
        case 2:
          if bandera_numeros_ingresados == False:
            print(" Ingrese un nu")
          else:
            resultado = sumar_numero 

        
          resultado = sumar()
          print("Sumando los numeros")
        case 3:
          print("Estoy restando")
        case 4:
          print("")
        case 5:
        case 6:
          bandera_seguir = False
          
    system("pause")
    system("cls")
        

