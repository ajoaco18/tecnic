# Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:
# En donde:
# mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
# mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
# mínimo: valor mínimo admitido (inclusive)
# máximo: valor máximo admitido (inclusive)
# reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

# En caso de que la función no haya podido conseguir un número válido, la misma retorna None.
# Repetir el mismo procedimiento para un dato de tipo float.





def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) ->int| None:
    
    numero = input(mensaje)          #Funcion con int, pide un int y da 3 intentos al error.
    numero = int(numero)
    
    for i in range(reintentos):
        while numero < minimo or numero > maximo:
            numero = input(f"Eror, {mensaje} ")
            numero = int(numero)
            break
            
    return numero

mensaje = get_int(f"Ingrese un numero: ", "Ingrese un numero: ", 1, 50, 3)




def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) ->int| None:
    
    numero = input(mensaje)       #Funcion con float, pide un float y da 3 intentos al error.
    numero = float(numero)
    
    for i in range(reintentos):
        while numero < minimo or numero > maximo:
            numero = input(f"Eror, {mensaje} ")
            numero = float(numero)
            break
            
    return numero

mensaje = get_float(f"Ingrese un numero: ", "Ingrese un numero: ", 1.0, 50.0, 3)


def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) ->int| None:
   
        numero = input(mensaje)       #Funcion con float, pide un float y da 3 intentos al error.
        numero = float(numero)
        
        while reintentos > 0 and (numero < minimo or numero > maximo):
            numero = input(f"Eror, {mensaje} ")
            numero = float(numero)
            reintentos -= 1

        return numero
   
    

mensaje = get_float(f"Ingrese un numero: ", "Ingrese un numero: ", 1.0, 50.0, 3)

# Ejercicio 2
def get_string(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> str | None:
    
    string = input(mensaje)
    string = len(string)
    if string == longitud:
        return string
    else:
        while reintentos > 0:
            string = input(mensaje_error)
            reintentos -= 1
            

            
validacion = get_string("Ingrese un string(cadena): ", "la longitud de caracter ingresada no es corrcta, vuelva a ingresarlo: ",5, 3)






    


