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
def validate_magic_cube(matrix:list, dimention:int, magic_number:int) -> bool: # se crea la funcion para validar que la matriz sea un cubo magico, con 3 parametros

    column_result_list = [0]*dimention # crea una lista para las columnas de tamaaño dimention, empezada con ceros, que es para almacenar los numeros de las sumas de las columnas
    line_result_list = [0]*dimention # para la fila lo mismo
    right_diagonal_result = 0 # inicio una variable para almacenar resultado de la suma diagonal derecha
    left_diagonal_result = 0 # y lo mismo para la izquierda izquierda

    ###SUMA COLUMNAS
    position_counter_column = -1 # arrancamos el contador en -1 porq si empezaba en 0 el ultimo valor de j no entraba, se quedaba uno atras.

    for j in range(len(matrix[0])): # itera sobre el rango de las columnas de la matriz
        position_counter_column += 1  # aumenta +1 al contador de posicion de  columnas

        column_result_list[position_counter_column] = listas_generales.column_addition(matrix, j) # calculo la suma de la columna actual con la funcion column_addition, q esta declarada en 
                                                                                                 # listas_generales, guarda el resultado en column_resul_list          
                                                                                                                                

    column_result = validate_magic_list(column_result_list,magic_number)  # colum_result verifica los resultados de las columnas son iguales al magic number

    ###SUMA FILAS
    position_counter_line = -1  #inicia un Contador para la posicion de lineas en -1, para realizar un seguimiento en q linea estamos sumando

    for i in range(len(matrix)): # itera sobre el rango de lineas de la matriz
        position_counter_line += 1 # aumenta +1 el contador de posicion de lineas

        line_result_list[position_counter_line] = listas_generales.line_addition(matrix,i) # se calcula la suma de la fila actual con la funcion line_addition, q esta declarada en listas_generales

    line_result = validate_magic_list(line_result_list, magic_number) # line_result lo que hace es verificar que el resultado de la lineas sean igual al resultados del number magic

    ###SUMA DIAGONAL DERECHA-IZQUIERDA
    right_diagonal_result = listas_generales.right_diagonal_addition(matrix) # calcula la suma de diagonal derecha a izquierda con la funcion right_diagonal_addition declarada en listas_generales

    ###SUMA DIAGONAL IZQUIERDA-DERECHA
    left_diagonal_result = listas_generales.left_diagonal_addition(matrix) # calcula la suma de diagonal izquierda a derecha con la funcion left_diagonal_addition declarada en listas_generales

    if column_result == line_result == right_diagonal_result == left_diagonal_result == magic_number: # copmprueba que los resultados de las columnas y filas, y diagonales sean igual al magic number,
        return True    # retorna true si los valores son iguales al numero magico
    else:
        return False # si no retorna false si los resultados no son iguales al del numero magico