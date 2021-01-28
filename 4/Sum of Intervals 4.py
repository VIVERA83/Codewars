
lst = [(1,5),(100, 200),(10, 6),(106, 19),(50, 110)]
# array = [[1,2],[6, 10],[11, 15]] #9
#array = [(1,4),(7, 10),(3, 5)] # 7
#array = [(1, 5), (1, 5)] #4

def sum_of_intervals(intervals):
    intervals.sort()
    intervals = [list(items) for items in intervals]
    i = 0
    while i < len(intervals) - 1:
        if intervals[i][1] >= intervals[i+1][0]:
             if intervals[i][1] < intervals[i+1][1]:
                 intervals[i][1] = intervals[i+1][1]
             del intervals[i+1]
        else:
            i += 1
    i = 0
    s = 0
    while i < len(intervals):
        s += intervals[i][1] - intervals[i][0]
        i += 1
    return s

#array.sort()
print(lst)

print(sum_of_intervals(lst))

# чужо1 код
def sum_of_intervals(intervals):
    return len(set([n for (a, b) in intervals for n in [i for i in range(a, b)]]))

def sum_of_intervals(intervals):
    times = []
    for time_ranges in intervals:
        print(time_ranges)
        for t in range(*time_ranges): # он сюда вводит значение множества их 2 1 начало 2 конец
            if t not in times:        #
                times.append(t)
    print(times)
    return len(times)

print(sum_of_intervals(lst))