def presentar_alumno(nombre: str, edad: int, altura: float)->int:
    """mostrar los datos de un alumno

    Args:
        nombre (str): nombre del alumno
        edad (int): edad del alumno
        altura (float): altura del  alumno

    Returns:
        int: (1: si esta todo bien / 0: si hubo un error)
    """
    print(f"Hola, me llamo {nombre}, tengo {edad} años y mido {altura}")
    return 1

presentar_alumno("Juan", 22, 1.75)

# def modificar_valor() -> None:
#     global numero
#     suma = 25 # local
#     numero = 45
#     print(numero)

# numero = 20 # global
# modificar_valor() 
# print(numero)

# def modificar_list(una_lista: list)->None:
#     una_lista[3] = "valor modificado."

# lista = [5, 9, 7, 6]
# print(lista)
# modificar_list(lista)
# print(lista)
