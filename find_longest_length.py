def search_repetitions(i, substring):
    if i == len(substring):
        return substring
    if len(substring) == 1:
        return substring
    char = substring[i]
    if char in substring[i + 1:]:
        j = i + 1
        while j < len(substring):
            if substring[j] == char:
                return search_repetitions(i + 1, substring[:j])
            j += 1
    else:
        if len(substring) > i + 1:
            return search_repetitions(i + 1, substring)
    return substring


def find_longest_length(string):
    list_substring = []
    i = 0
    while i < len(string):
        list_substring.append(search_repetitions(0, string[i:]))
        i += 1
    max = 0
    for x in list_substring:
        if len(x) > max:
            max = len(x)
    return max


print(find_longest_length('') == 0)
print(find_longest_length('a') == 1)
print(find_longest_length('jabjcdel') == 7)
print(find_longest_length('abcddef') == 4)
print(find_longest_length('abbccddeffg') == 3)
print(find_longest_length('abcd') == 4)
print(find_longest_length('1234561qweqwer') == 9)
