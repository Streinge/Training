def transposed(matrix):
    col = 0
    transported_matrix = []
    while col < len(matrix[0]):
        row = 0
        new_string = []
        while row < len(matrix):
            new_string.append(matrix[row][col])
            row += 1
        transported_matrix.append(new_string)
        col += 1
    return transported_matrix


print(transposed([[1]]))  # [[1]]
print(transposed([[1, 2], [3, 4]]))  # [[1, 3], [2, 4]]
print(transposed([[1, 2], [3, 4], [5, 6]]))  # [[1, 3, 5], [2, 4, 6]]
print(transposed(transposed([[1, 2]])) == [[1, 2]])  # True
