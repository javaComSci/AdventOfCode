def part1():
    data_file = open("data.txt", "r")

    p = 0
    for line in data_file.readlines():
        low = 0
        up = 127
        j = 0

        # get the row
        for i in range(7):
            if line[i] == "F":
                up = int((low + up)/2)
            else:
                low = int((low + up)/2)

        # get the col
        left = 0
        right = 8
        for i in range(3):
            if line[7+i] == "R":
                left = int((left + right)/2)
            else:
                right = int((left + right)/2)


        j = up * 8 + left
        
        p = max(j, p)
    
    print(p)


def part2():
    data_file = open("data.txt", "r")

    p = []
    for line in data_file.readlines():
        low = 0
        up = 127
        j = 0

        # get the row
        for i in range(7):
            if line[i] == "F":
                up = int((low + up)/2)
            else:
                low = int((low + up)/2)

        # get the col
        left = 0
        right = 8
        for i in range(3):
            if line[7+i] == "R":
                left = int((left + right)/2)
            else:
                right = int((left + right)/2)


        j = up * 8 + left
        
        p.append(j)
    
    p.sort()

    for i in range(1, len(p) - 1):
        if p[i] + 1 != p[i+1]:
            print(p[i], p[i+1])
            break
    
    # print(p)


part2()