###SUMA COLUMNAS
def column_addition(matrix:list, column:int) -> int|float:
    result = 0

    for i in range(len(matrix)):
        result += matrix[i][column]

    return result

###SUMA FILAS
def line_addition(matrix:list, line:int) -> int|float:
    result = 0

    for j in range(len(matrix[line])):
        result += matrix[line][j]

    return result

###SUMA DIAGONAL DERECHA-IZQUIERDA
def right_diagonal_addition(matrix:list) -> int|float:

    result = 0

    for i in range(len(matrix)):
        result += (matrix[i][i])
         
    return result

###SUMA DIAGONAL IZQUIERDA-DERECHA
def left_diagonal_addition(matrix:list) -> int|float:

    result = 0

    position_counter = -1

    for i in range(len(matrix)-1, -1, -1):
        
        position_counter += 1
        result += (matrix[i][position_counter])
    
    return result