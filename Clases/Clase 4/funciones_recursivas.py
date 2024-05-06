
# 111-1 Joaquin Aguero Funciones recursivas

from Package_Funciones_.Input import get_int


# 1) Realizar una función recursiva que calcule la suma de los primeros números naturales:


def sumar_naturales(numero: int)-> int:
    if numero == 0:
        resultado = 0
    else:
        resultado = numero + sumar_naturales(numero - 1)
    return resultado

numero = 5
sumar = sumar_naturales(numero)
print(f"La suma de {numero} es: {sumar}")
#####################################################################################################

#2) Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia(base: int, exponente: int) -> int:
    if base <= 0:
        resultado = 1
    
    else:
        resultado = base  ** exponente

    return resultado

base = 5
exponente = 2

potencia = calcular_potencia(base, exponente)
print(f"La potencia del numero: {base}, de exponente {exponente}, es: {potencia}")

#####################################################################################################

#3) Realizar una función recursiva que la suma de los dígitos de un número:

def sumar_digitos(numero: int) -> int:
    if numero < 10:
        return numero
    else:
        return numero % 10 + sumar_digitos(numero // 10)
    
numero = 333
resultado = sumar_digitos(numero)
print(f"La suma de los digitos es: {resultado}")



################################################################################



#Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

def calcular_fibonacci(numero: int) -> int:
    if (numero == 0 or numero == 1):
      return numero
      
    else:
      
      return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

    
mensaje = get_int(f"Ingrese un numero: ", "Ingrese un numero: ", 1, 50, 3)
mensaje = int(mensaje)

resultado = calcular_fibonacci(mensaje)
print(resultado)







