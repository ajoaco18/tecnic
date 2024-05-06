from Package_Input.Input import *
from Package_Input.Validate import *
numero_ingresado = get_int("Ingrese un numero del 1 al 50: ")
validar_numero = validate_number(numero_ingresado, 1, 50, "Eror, El numero debe ser del 1 al 50. \n Ingrese nuevamente un numero: ", 3)
print(validar_numero)

string = get_string("ingrese una cadena (texto): ")
validar_longitud = validate_lenght(string, 5, "Error, ingrese nuevamente una cadena de 5 caracteres: ", 3)
print(validar_longitud)