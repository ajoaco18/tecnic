 ########## CREAR MATRIZ DESDE TECLADO #####

# filas = int(input("Ingrese el numero de filas que quiere en su matriz: "))
# columnas = int(input("Ingrese el numero de columnas que quiere en su matriz: "))
# matrix = []

# for filas_posicion in range(filas):
#     fila = []
#     for i in range(columnas):
#         fila.append(int(input(f"Introduce un elementoi a la fila {filas_posicion}: ")))
#     matrix.append(fila)
# for fila in matrix:
#     print(fila)



########### SUMA DE MATRICES ############

matrix_a = [[1, 2, 3],
            [1, 2, 3],
            [5, 6, 7],]

matrix_b = [[12, 23, 31],
            [51, 42, 33],
            [5, 66, 7],]

matrix_c = []

for i in range(len(matrix_a)): # longitud de filas
    new_row = []
    for j in range(len(matrix_a[0])): #logitud columna pos 0
        new_row.append(matrix_a[i][j] + matrix_b[i][j])
    matrix_c.append(new_row)
for i in range(len(matrix_a)):
    print(f"{matrix_a[i]}   {matrix_b[i]}  {matrix_c[i]}")
    


    