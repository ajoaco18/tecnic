# Joaquin Aguero 111-1 
# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
def numero():
    valor = int(input("Ingrese un numero: "))
    
    return valor
    
numero_ingresado = numero()
print(f"Numero ingresado: {numero_ingresado}")