def snail_path(matrix):
    if len(matrix) == 0:
        return False
    sum_list = []
    i = 0
    j_max = -1
    i_max = -1
    while len(matrix) >= 1:
        for item in matrix[i]:
            sum_list.append(item)
        del matrix[i]
        for item in matrix:
            if item != []:
                sum_list.append(item[j_max])
                del item[j_max]
            else:
                break
        if matrix != []:
            matrix[i_max].reverse()
            for item in matrix[i_max]:
                sum_list.append(item)
            del matrix[i_max]
        else:
            break
        matrix.reverse()
        for item in matrix:
            if item != []:
                sum_list.append(item[i])
                del item[i]
            else:
                break
        matrix.reverse()
        if len(matrix) == 0:
            break
    return sum_list


print(not snail_path([]))
print(not snail_path([[]]))
print(snail_path([[0]]) == [0])
print(snail_path([[1, 2, 3]]) == [1, 2, 3])
print(snail_path([[1], [2], [3], [4]]) == [1, 2, 3, 4])
print(snail_path([
    [1, 2],
    [3, 4],
]) == [1, 2, 4, 3])
print(snail_path([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])

print(snail_path([
    [None, 0, True],
    [-1, '', False],
    [[], 'foo', object],
]) == [None, 0, True, False, object, 'foo', [], -1, ''])
