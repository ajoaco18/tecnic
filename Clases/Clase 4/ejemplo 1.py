# for i in range(10):
#     print ("hola")

# def cuenta_regresiva(iteraciones)-> int:
#     if iteraciones != 0:
#         print(iteraciones)
#         cuenta_regresiva(iteraciones -1)
#     return iteraciones

# cuenta_regresiva(10)

# def cuenta_regresiva(iteraciones) -> None:
#     if iteraciones != -1:
#         print(iteraciones)
#         iteraciones -= 1
#         cuenta_regresiva(iteraciones)


# cuenta_regresiva(10)

# numero = 5
# factorial = 1             
# for i in range (1, numero + 1):
#     factorial *= i           # Hace factorial

# print(f"el factorial de {numero} es : {factorial}")


def calcular_factorial(numero)-> int:
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1)
    
    return resultado
    
    
    
numero = 5 
factorial = calcular_factorial(numero)

    
print(f"el factorial de {numero} es : {factorial}")





