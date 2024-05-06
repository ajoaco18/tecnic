from Package_input import listas_generales

def validate_number(number:int|float, minimum:int|float, maximum:int|float) -> bool:
    if number >= minimum and number <= maximum:
        return True
    else:
        return False

def validate_length(string:str, length:int) -> bool:
    if len(string) == length:
            return True
    else:
        return False

###VALIDA QUE TODOS LOS ELEMENTOS DE UNA LISTA SEAN IGUAL A NÚMERO MÁGICO
def validate_magic_list(array:list, magic_number:int) -> int|bool:
    array_length = len(array)

    magic_number_counter = 0

    for i in range(array_length):
        if array[i] == magic_number:
            magic_number_counter += 1
    
    if magic_number_counter == array_length:
        return magic_number
    else:
        return False

###VALIDA CUBO MÁGICO    
def validate_magic_cube(matrix:list, dimention:int, magic_number:int) -> bool:

    column_result_list = [0]*dimention
    line_result_list = [0]*dimention
    right_diagonal_result = 0
    left_diagonal_result = 0

    ###SUMA COLUMNAS
    position_counter_column = -1

    for j in range(len(matrix[0])):
        position_counter_column += 1

        column_result_list[position_counter_column] = listas_generales.column_addition(matrix, j)

    column_result = validate_magic_list(column_result_list,magic_number)

    ###SUMA FILAS
    position_counter_line = -1

    for i in range(len(matrix)):
        position_counter_line += 1

        line_result_list[position_counter_line] = listas_generales.line_addition(matrix,i)

    line_result = validate_magic_list(line_result_list, magic_number)

    ###SUMA DIAGONAL DERECHA-IZQUIERDA
    right_diagonal_result = listas_generales.right_diagonal_addition(matrix)

    ###SUMA DIAGONAL IZQUIERDA-DERECHA
    left_diagonal_result = listas_generales.left_diagonal_addition(matrix)

    if column_result == line_result == right_diagonal_result == left_diagonal_result == magic_number:
        return True
    else:
        return False