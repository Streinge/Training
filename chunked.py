def chunked(size, sequence):
    i = 1
    new_list = []
    while i <= len(sequence):
        start = i - 1
        if size - 1 + i <= len(sequence):
            finish = size - 1 + i
            new = sequence[start:finish]
        else:
            new = sequence[start:]
        new_list.append(new)
        i += size
    return new_list


print(chunked(2, ['a', 'b', 'c', 'd']))  # [['a', 'b'], ['c', 'd']]
print(chunked(3, ['a', 'b', 'c', 'd']))  # [['a', 'b', 'c'], ['d']]
print(chunked(3, 'foobar'))  # ['foo', 'bar']
print(chunked(10, (42,)))  # [(42,)]