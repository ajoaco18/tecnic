# Joaquin Aguero 111-1
# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
def potencia():
    base = int(input("Ingrese el numero que quiere poner en la base: "))
    exponente = int(input("Ingrese el numero que quiere poner de exponente: "))
    resultado = base ** exponente
    return resultado

resultado_potencia = potencia()
print(f"El resultado de su potencia es: {resultado_potencia}.")