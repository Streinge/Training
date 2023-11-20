def is_continuous_sequence(list):
    if len(list) < 2:
        return False
    for i, item in enumerate(list[:-1]):
        if list[i + 1] - item != 1:
            return False
    return True


"""print(is_continuous_sequence([10, 11, 12, 13]) == True)
print(is_continuous_sequence([-5, -4, -3]) == True)
print(is_continuous_sequence([10, 11, 12, 14, 15]) == False)
print(is_continuous_sequence([1, 2, 2, 3]) == False)
print(is_continuous_sequence([7]) == False)
print(is_continuous_sequence([]) == False)"""
print(not is_continuous_sequence([]))
print(not is_continuous_sequence([7]))
print(not is_continuous_sequence([5, 3, 2, 8]))
print(not is_continuous_sequence([10, 11, 12, 14, 15]))
print(not is_continuous_sequence([10, 11, 11, 12]))
print(not is_continuous_sequence([5, 6, 6, 8]))
print(is_continuous_sequence([0, 1, 2, 3]))
print(is_continuous_sequence([-5, -4, -3]))
print(is_continuous_sequence([10, 11, 12, 13]))
