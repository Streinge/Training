def show(image):
    for line in image:
        print(line)

def enlarge(list1):
    list_new = []
    for string in list1:
        i = 0
        new_string = ''
        while i < len(string):
            new_string = new_string + string[i] * 2
            i += 1
        list_new.append(new_string)
    list_extended = []
    for string in list_new:
        list_extended.extend([string, string])
    return list_extended

dot = ['@']
show(enlarge(dot))
frame = [
    '****',
    '*  *',
    '*  *',
    '****'
]

show(frame)

show(enlarge(frame))
