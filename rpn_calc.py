def rpn_calc(list_enter):
    while len(list_enter) > 1:
        i = 0
        while i < len(list_enter):
            if str(list_enter[i]) in '+-*/':
                expression = f'{str(list_enter[i-2])} {list_enter[i]} {str(list_enter[i-1])}'
                result = eval(expression)
                list_enter.insert(i + 1, result)
                del list_enter[i-2:i+1]
                break
            i += 1
    return list_enter[0]


print(rpn_calc([1, 2, '+', 4, '*', 3, '+']))  # 15
print(rpn_calc([7, 2, 3, '*', '-']))  # 1