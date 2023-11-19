def mirror_matrix(matrix):
    if len(matrix) < 2:
        return
    for row in matrix:
        i = 0
        j = -1
        while i < len(row) // 2:
            row[j] = row[i]
            i += 1
            j -= 1
    return matrix

l = [[42]]


print(mirror_matrix(l) is None)
