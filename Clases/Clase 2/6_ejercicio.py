# Joaquin Aguero 111-1
# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def par_impar(valor):
    if valor % 2 == 0:
        mensaje = "El numero ingresado es par."
    else:
        mensaje = "El numero ingresado es impar."
    return mensaje

valor = int(input("Ingrese un numero: "))
print(par_impar(valor))
