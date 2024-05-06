def validate_number(numero: int, mensaje_error: str,  minimo: int, maximo: int, reintentos: int) -> int:
    numero = int(numero)
    while reintentos > 0 and (numero < minimo or numero > maximo):
        numero = input(mensaje_error)
        numero = int(numero)
        reintentos -= 1
    return numero
# mensaje = validate_number(f"Ingrese un numero: ", "Ingrese un numero: ", 1, 50, 3)

def validate_lenght(string: str, mensaje_error: str, longitud: int, reintentos: int) -> str | None:
    string = len(string)
    if string == longitud:
        return string
    else:
        while reintentos > 0:
            string = input(mensaje_error)
            reintentos -= 1

# validacion = get_string("Ingrese un string(cadena): ", "la longitud de caracter ingresada no es corrcta, vuelva a ingresarlo: ",5, 3)


