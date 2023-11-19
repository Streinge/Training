from collections import Counter


def visualize(tuple, bar_char='₽'):
    c = sorted(Counter(tuple).most_common())
    string_sum = ''
    max = 0
    string1 = ''
    string2 = ''
    for x in c:
        if x[1] > max:
            max = x[1]
        if x == c[-1]:
            string1 = string1 + '--'
        else:
            string1 = string1 + '---'
        whitespace = ' '
        if x == c[-1]:
            whitespace = ''
        if len(str(x[0])) == 1:
            string2 = string2 + str(x[0]) + ' ' + whitespace
        else:
            string2 = string2 + str(x[0]) + '' + whitespace

    j = 0
    while j <= max:
        i = 0
        string = ''
        whitespace = ' '
        while i < len(c):
            if i == len(c) - 1:
                whitespace = ''
            if c[i][1] == max - j:
                string = string + str(c[i][1]) + ' ' + whitespace
            elif c[i][1] < max - j:
                string = string + '  ' + whitespace
            elif c[i][1] > max - j:
                string = string + bar_char * 2 + '' + whitespace
            i += 1
        if string != '':
            string_sum = string_sum + string + '\n'
        j += 1
    string_sum = string_sum + string1 + '\n' + string2
    return string_sum

MONEY = (
    1, 20, 2, 5, 20,
    3, 5, 2, 10, 2,
    20, 2, 20, 1, 2,
    1, 1, 2, 10, 20, 3,
)

print(visualize(MONEY))
print("""
   6             
   ₽₽          5 
4  ₽₽          ₽₽
₽₽ ₽₽          ₽₽
₽₽ ₽₽ 2  2  2  ₽₽
₽₽ ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
₽₽ ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
-----------------
1  2  3  5  10 20
"""[1:-1])