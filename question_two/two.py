#Takes a matrix and calculates the difference between diagonals

MIN_MATRIX_SIZE = 2
MAX_MATRIX_SIZE = 1000

class SizeError(Exception):
    pass

#Alias
Matrix = list[list[int]]

def difference_of_diagonals(matrix: Matrix):
    size = len(matrix)
    if size < MIN_MATRIX_SIZE or size > MAX_MATRIX_SIZE:
        raise SizeError(f'Matrix size less than {MIN_MATRIX_SIZE} or bigger than {MAX_MATRIX_SIZE}')
    sum_left_diagonal = 0
    sum_right_diagonal = 0

    for index in range(size):
        reverse_index = -(index+1)

        sum_left_diagonal += matrix[index][index]
        sum_right_diagonal += matrix[reverse_index][index]

    difference = sum_left_diagonal - sum_right_diagonal
    
    #Since it's modular value, it's always positive
    return abs(difference)
