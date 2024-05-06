
# Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
lista = [1,5,4,6,7,10]
def calcular_promedio(lista: list)-> float:
    for i in range(len(lista)):
        suma = sum(lista)
        cantidad = len(lista)
        promedio = suma / cantidad

    return promedio

resultado = calcular_promedio(lista)
print(f"El promedio de {lista}, es: {resultado}")

# Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.

lista = [1,5,-4,6,-7,10]
def promedio_positivo(lista: list) -> float:
    for i in range(len(lista)):
        if lista[i] > 0:
            suma = sum(lista)
            cantidad = len(lista)
            promedio = suma / cantidad
    return promedio


resultado = promedio_positivo(lista)
print(f"El promedio de {lista}, es: {resultado}")


# Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
lista = [2,2,2]
def calcular_producto(lista: list)-> int:
    producto = 1
    for i in lista:
        producto = producto * i

    return producto

resultado =  calcular_producto(lista)
print(f"El producto de {lista}, es: {resultado}")


# Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
lista = [2,2,9]

def valor_max(lista: list)-> int:
    bandera_maximo = True
    posicion = 0
    for i in range(len(lista)):
        if bandera_maximo == True:
            numero_maximo = lista[i]
            bandera_maximo = False
            posicion = i
        elif numero_maximo < lista[i]:
            numero_maximo = lista[i]
        
        mensaje = f"pos: {i}, valor: {numero_maximo}"
        
    return mensaje



resultado = valor_max(lista)
print(resultado)

        
# Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, 
# un nombre a reemplazar y su correspondiente reemplazo. La función debe reemplazar cada ocurrencia 
# del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados.
lista = ["Juan", "María", "Carlos", "Laura", "Pedro"]
def reemplazar_nombres(lista: list):
    nombre = "Juan"
    nombre_remplazo = "Joa"
    contador_reemplazos = 0
    for i in range(len(lista)):
        if lista[i] == nombre:
            lista[i] = nombre_remplazo
            contador_reemplazos +=1
    return contador_reemplazos
    
remplazador = reemplazar_nombres(lista)

print(f"Lista{lista}, lista con reemplazo {remplazador}")


    
    

    



