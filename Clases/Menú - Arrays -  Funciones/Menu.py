from Package_Input.Input import *
from Package_Arrays.Array_Generales import *
from os import system


bandera_seguir = True
bandera_numeros_ingresados = False
numeros = [0] * 10 # Se le pone limite de 10 numeros a la lista.

while bandera_seguir:
    opcion = int(input("1.Ingresar datos"
                       "\n2.Cantidad de números positivos y negativos."
                       "\n3.Mostrar la sumatoria de ros palos númeres."
                       "\n4.Informar el mayor de los números impares."
                       "\n5.Listar todos los números ingresados"
                       "\n6.Listar todos los números pares."
                       "\n7.Listar los números de las posiciones impares."
                       "\n8.Salir"
                       "\nElija Una opcion: "))
    match opcion:
        case 1:
         # Pedir el ingreso de 10 números enteros entre -1000 y 1000.
          for i in range(10):
            numero = get_int(f"{i+1}.Ingrese un numero: :  ", "Error!, Ingrese nuevamente un numero", -1000, 1000, 3)
            if -1000 <= numero <= 1000:
              numeros[i] = numero  # Agrega el numero a la lista de numeros.
        case 2:
          # Mostrar la cantidad de números positivos y negativos.
          positivos, negativos = num_positivo_negativo(numeros)
          print(f"Cantidad de numeros positivos: {positivos}.\n"
                f"Cantidad de numeros negativos: {negativos}.")
          
        case 3:
          # Mostrar la sumatoria de los números pares.
          total_sum_pares = sumatoria_pares(numeros)
          print(f"La sumatoria de los numeros pares es: {total_sum_pares}")

        case 4:
          # Informar el mayor de los números impares.
          numero_impar_mayor = max_impares(numeros)
          print(f"El numero maximo impar es: {numero_impar_mayor}")
        case 5:
        # Listar todos los números ingresados.
          lista_numeros = numeros_listas(numeros)
          print(f"Los numeros ingresado en la lista son: {lista_numeros}")
        case 6:
          # Listar todos los números pares.
          lista_numeros_pares = todos_num_pares(numeros)
          print(f"Lista de numeros ingresados: {lista_numeros_pares}")
      
        
        case 7:
          # Listar los números de las posiciones impares
          lista_posicion_impares = posiciones_impares(numeros)
          print(lista_posicion_impares)
    
        case 8:
          bandera_seguir = False 
          system("pause")
          system("cls")
     

         

