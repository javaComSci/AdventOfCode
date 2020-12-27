from collections import Counter

def part1():
    data_file = open("data.txt", "r")

    vals = [0]
    for line in data_file.readlines():
        vals.append(int(line.strip()))
    vals.sort()
    vals.append(max(vals) + 3)
    
    diffs = []
    for i in range(len(vals) - 1):
        diffs.append(vals[i+1] - vals[i])
    
    print(diffs)
    c = Counter(diffs)

    print(c[1] * c[3])

seen_ways = {}

def get_ways(n, vals):
    print("GET FOR", n)
    if n in seen_ways:
        return seen_ways[n]
    
    if n not in vals:
        return 0
    
    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    ways = get_ways(n - 3, vals) + get_ways(n - 2, vals) + get_ways(n - 1, vals)
    seen_ways[n] = ways
    return ways

def part2():
    data_file = open("data.txt", "r")

    vals = [0]
    for line in data_file.readlines():
        vals.append(int(line.strip()))
    vals.sort()
    vals.append(max(vals) + 3)

    print(get_ways(max(vals), vals))

    # get the different ways to go from 0 to the max num
    # ways[22] = ways[22 - 1] + ways[22 - 2] + ways[22 - 3]
    # ways[1] = ways[0] 
    # ways[7] = ways[4] + ways[5] + ways[6] (if exist)


part2()