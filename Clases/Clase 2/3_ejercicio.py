# Joaquin Aguero 111-1 
# Crear una función que le solicite al usuario el ingreso de una cadena y la retorna. 
def ingreso():
    ingreso_cadena = str(input("Ingrese una palabra / oracion: "))
    return ingreso_cadena

cadena = ingreso()
print(f"Palabra / oracion ingresada: {cadena}.")
