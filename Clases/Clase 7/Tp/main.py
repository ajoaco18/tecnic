from Package_input import get_int
from Package_input import Validate

DIMENTION = 3

magic_number = int(DIMENTION*(DIMENTION*DIMENTION + 1)/2)

flag_valid_matrix = True

message_input = "Ingrese los valores de la matriz: "
message_input_error = "Ingrese los valores de la matriz (el valor debe estar entre -1000 y 1000): "
message_input_error_trys = "Agotó los intentos. Vuelva a iniciar."
message_final_magic_cube = "Esta matriz es un cubo mágico!! :D"
message_final_no_magic_cube = "Esta matriz no es un cubo mágico. :/"

###ENTRADA MATRIZ
matrix_entry = [[0] * DIMENTION for _ in range(DIMENTION)]

for i in range(len(matrix_entry)):
    for j in range(len(matrix_entry[i])):
        matrix_entry[i][j] = get_int(message_input, message_input_error, -1000, 1000, 5)
        if matrix_entry[i][j] == None:
            print(message_input_error_trys)
            break
    if matrix_entry[i][j] == None:
        break

###VALIDAR MATRIZ
for i in range(len(matrix_entry)):
    for j in range(len(matrix_entry[i])):
        if matrix_entry[i][j] == None:
            flag_valid_matrix = False

###IMPRIME MATRIZ
if flag_valid_matrix:

    for i in range(len(matrix_entry)):
        for j in range(len(matrix_entry[i])):
            print(matrix_entry[i][j], end = " ")
        print("")

    if Validate.validate_magic_cube(matrix_entry,DIMENTION, magic_number):
        print(message_final_magic_cube)
    else:
        print(message_final_no_magic_cube)