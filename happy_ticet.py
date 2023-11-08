def is_happy_ticket(str_number):
    number_length  = len(str_number)
    sum_begin = 0
    sum_end = 0
    for i in range(0, number_length // 2):
        sum_begin += int(str_number[i])
    for i in range((number_length // 2), number_length):
        sum_end += int(str_number[i])
    if sum_begin == sum_end:
        return True
    return False

print(is_happy_ticket('12344321'))
