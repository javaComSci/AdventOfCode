def does_add(vals, sum_needed):
    vals.sort()
    l = 0
    r = len(vals) - 1
    while l < r:
        if vals[l] + vals[r] < sum_needed:
            l += 1
        elif vals[l] + vals[r] > sum_needed:
            r -= 1
        else:
            return True

    return False

def part1():
    data_file = open("data.txt", "r")

    vals = []
    for line in data_file.readlines():  
        val = int(line.strip())
        vals.append(val)

    for i in range(25, len(vals)):
        v = does_add(vals[i-25:i], vals[i])
        if v ==  False:
            print(vals[i])
            return (vals, vals[i], i)

def part2(vals, val, v):
    print(v)
    cont_vals = None
    for i in range(len(vals)):
        acc = vals[i]
        start = i
        end = None
        for j in range(i + 1, len(vals)):
            if acc + vals[j] == val:
                end = j
                break
            elif acc + vals[j] > val:
                break
            acc += vals[j]
        if end != None:
            cont_vals = vals[start:end]
            break
    print(max(cont_vals) + min(cont_vals))

    


vals, val, i = part1()
part2(vals, val, i)