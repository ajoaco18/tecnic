# Joaquin Aguero 111-1
# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def maximo(prim_num, seg_num, ter_num):
    maximo = max(prim_num, seg_num, ter_num)
    print(f"El mayor de {prim_num}, {seg_num}, {ter_num}, es: {maximo}.")
    return maximo

maximo(5, 8, 55)
    
    
