# Joaquin Aguero 111-1
#Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
def area():
    ingreso_radio = float(input("Ingrese el radio en cm de su circulo: "))
    radio = ingreso_radio ** 2
    resultado = 3.14 * radio
    return resultado
resultado_area = area()
print(f"El area de su circulo es: {resultado_area}cm2")