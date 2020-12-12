
# You are given a 2D matrix as input. Write a function transpose(matrix)
#  which computes and returns the transposed matrix.
# Input: matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
# Return: matrix_transposed = [[1, 4], [2, 5], [3, 6], [4, 8]]

matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

def transpose(matrix):
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))] 
    print("the transposed matrix is : ") 
    for matrix in transpose: 
        print(matrix) 

transpose(matrix)