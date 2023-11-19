def hamming_weight(number):
    binary = bin(number)
    count = 0
    for x in binary:
        if x == '1':
            count += 1
    return count


print(hamming_weight(0))  # 0
print(hamming_weight(4))  # 1
print(hamming_weight(101))  # 4