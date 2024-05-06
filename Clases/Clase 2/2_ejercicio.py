# Joaquin Aguero 111-1 
# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
def numero():
    numero_usuario = float(input("Ingrese un numero flotante(numero con coma): "))
    return numero_usuario

numero_ingresado = numero()
print(f"Numero flotante ingresado: {numero_ingresado}")

