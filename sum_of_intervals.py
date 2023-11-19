
def checked_intersections(intervals):
    result_list = []
    while len(intervals) != 1:
        new_list = []
        for i, interval in enumerate(intervals[:-1]):
            if interval[1] > intervals[i + 1][0]:
                new_list.append([min(interval[0], intervals[i + 1][0]), max(interval[1], intervals[i + 1][1])])
                del intervals[i:i + 2]
                new_list.extend(intervals)
                intervals = new_list
                break
            else:
                result_list.append(interval)
                del intervals[0]
                break
    result_list.extend(intervals)
    return result_list


def sum_of_intervals(intervals):
    intervals.sort()
    sum = 0
    for interval in checked_intersections(intervals):
        sum = sum + (interval[-1] - interval[0])
    return sum


print(sum_of_intervals([[1, 1],]))  # 0

print(sum_of_intervals([
    [1, 2],
    [50, 100],
    [60, 70],
]))
# 51
print(sum_of_intervals([
    [1, 2],
    [5, 10],
]))
# 6
print(sum_of_intervals([[5, 5]]) == 0)
print(sum_of_intervals([[3, 10]]) == 7)
print(sum_of_intervals([
        [1, 2],
        [11, 12],
    ]) == 2)
print(sum_of_intervals([
        [2, 7],
        [6, 6],
    ]) == 5)

print(sum_of_intervals([
        [1, 5],
        [1, 10],
    ]) == 9)

print(sum_of_intervals([
        [1, 9],
        [7, 12],
        [3, 4],
    ]) == 11)

print(sum_of_intervals([
        [7, 10],
        [1, 4],
        [2, 5],
    ]) == 7)

print(sum_of_intervals([
        [1, 5],
        [9, 19],
        [1, 7],
        [16, 19],
        [5, 11],
    ]) == 18)

print(sum_of_intervals([
        [1, 3],
        [20, 25],
    ]) == 7)