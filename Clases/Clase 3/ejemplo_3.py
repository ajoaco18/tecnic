
def get_int(mensaje: str, min: int, max: int) ->int:
    numero = input(mensaje)
    numero = int(numero)
    while numero < min or numero > max:
        numero = input(f"Eror, {mensaje} ")
        numero = int(numero)
    return numero

# numero_solicitado = get_int()

# print(f"El numero ingresado es: {numero_solicitado}")
edad = get_int("Ingrese su edad: ", 18, 30) # 18 - 30
if(edad!=None):
    legajo = get_int("Ingrese su legajo: ", 1000, 2000) # 1000 - 2000
    nota = get_int("Ingrese su nota: ", 1, 10) # 1 - 10







