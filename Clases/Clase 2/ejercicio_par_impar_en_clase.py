# Funcion detecta par e impar.
def par_impar(num_ingresado):
    if num_ingresado % 2 == 0:
        mensaje = "Es par"
    else:
        mensaje = "es impar"
    return mensaje
    
num_ingresado = int(input("Ingresa un numero: "))
print(par_impar(num_ingresado))