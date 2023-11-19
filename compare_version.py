def compare_version(version1, version2):
    version1 = version1.split('.')
    version2 = version2.split('.')
    if int(version1[0]) > int(version2[0]):
        return 1
    elif int(version2[0]) > int(version1[0]):
        return -1
    elif int(version2[0]) == int(version1[0]):
        if int(version1[1]) > int(version2[1]):
            return 1
        elif int(version2[1]) > int(version1[1]):
            return -1
        elif int(version2[1]) == int(version1[1]):
            return 0


print(compare_version('0.1', '0.2') == -1)

print(compare_version('0.2', '0.1') == 1)
print(compare_version('4.2', '4.2') == 0)
print(compare_version('0.2', '0.12') == -1)
print(compare_version('3.2', '4.12') == -1)
print(compare_version('3.2', '2.12') == 1)
