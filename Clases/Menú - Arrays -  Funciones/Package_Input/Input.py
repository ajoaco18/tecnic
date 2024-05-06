# get_int()
# get_float()
# get_string()
#

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) ->int| None:
    numero = input(mensaje)
    numero = int(numero)
    while reintentos > 0 and (numero < minimo or numero > maximo):
        numero = input(f"Error, {mensaje}")
        numero = int(numero)
        reintentos -= 1
    return numero
# mensaje = get_int(f"Ingrese un numero: ", "Ingrese un numero: ", 1, 50, 3)



def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) ->float| None:
   
    numero = input(mensaje)       #Funcion con float, pide un float y da 3 intentos al error.
    numero = float(numero)
        
    while reintentos > 0 and (numero < minimo or numero > maximo):
        numero = input(f"Eror, {mensaje} ")
        numero = float(numero)
        reintentos -= 1

    return numero

# mensaje = get_float(f"Ingrese un numero: ", "Ingrese un numero: ", 1.0, 50.0, 3)

def get_string(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> str | None:
    
    string = input(mensaje)
    string = len(string)
    if string == longitud:
        return string
    else:
        while reintentos > 0:
            string = input(mensaje_error)
            reintentos -= 1

# validacion = get_string("Ingrese un string(cadena): ", "la longitud de caracter ingresada no es corrcta, vuelva a ingresarlo: ",5, 3)