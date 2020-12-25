def part1():
    data_file = open("data.txt", "r")

    group = []
    count = 0
    for line in data_file.readlines():
        l = [k for k in line.strip().split()]
        if len(l) == 0:
            count += len(set(group))
            group = []
        else:
            for i in l[0]:
                group.append(i)
    count += len(set(group))
    print(count)

def part2():
    data_file = open("data.txt", "r")

    group = []
    count = 0
    for line in data_file.readlines():
        l = [k for k in line.strip().split()]
        if len(l) == 0:
            s = set.intersection(*group)
            count += len((s))
            group = []
        else:
            group.append(set(l[0]))
    s = set.intersection(*group)
    count += len((s))
    print(count)


part2()