def get_occupied_count(arr, i, j):
    occupied_count = 0
    if i-1 >= 0 and j-1 >= 0:
        if arr[i-1][j-1] == "#":
            occupied_count += 1
    if i-1 >= 0 and j >= 0:
        if arr[i-1][j] == "#":
            occupied_count += 1
    if i-1 >= 0 and j+1 < len(arr[0]):
        if arr[i-1][j+1] == "#":
            occupied_count += 1
    if i >= 0 and j-1 >= 0:
        if arr[i][j-1] == "#":
            occupied_count += 1
    if i >= 0 and j+1 < len(arr[0]):
        if arr[i][j+1] == "#":
            occupied_count += 1
    if i+1 < len(arr) and j-1 >= 0:
        if arr[i+1][j-1] == "#":
            occupied_count += 1
    if i+1 < len(arr) and j >= 0:
        if arr[i+1][j] == "#":
            occupied_count += 1
    if i+1 < len(arr) and j+1 < len(arr[0]):
        if arr[i+1][j+1] == "#":
            occupied_count += 1
    return occupied_count


def mutate(arr):
    new_arr = []

    mutated = False
    occ = 0
    for i in range(len(arr)):
        curr_row = []
        for j in range(len(arr[0])):
            if arr[i][j] == ".":
                curr_row.append(".")
            elif arr[i][j] == "L":
                if get_occupied_count(arr, i, j) == 0:
                    curr_row.append("#")
                    occ += 1
                    mutated = True
                else:
                    curr_row.append("L")
            elif arr[i][j] == "#":
                if get_occupied_count(arr, i, j) >= 4:
                    curr_row.append("L")
                    mutated = True
                else:
                    occ += 1
                    curr_row.append("#")
        new_arr.append(curr_row)
    # for j in range(len(new_arr)):
    #     print("".join(new_arr[j]))
    # print("\n")
    return (mutated, new_arr, occ)

def part1():
    data_file = open("data.txt", "r")

    arr = []
    for line in data_file.readlines():
        row = [i for i in line.strip()]
        arr.append(row)
   
    while True:
        mutated, new_arr, occ = mutate(arr)
        arr = new_arr
        if mutated == False:
            break

    print(occ)


top_left = {}
top_mid = {}
top_right = {}
mid_left = {}
mid_right = {}
bot_left = {}
bot_mid = {}
bot_right = {}

def get_top_left_and_bot_right(arr, i, j):
    if (i,j) not in top_left:
        if i-1 >= 0 and j-1 >= 0:
            if arr[i-1][j-1] != ".":
                top_left[(i,j)] = (i-1, j-1)
                bot_right[(i-1, j-1)] = (i,j)
            else:
                get_top_left_and_bot_right(arr, i-1, j-1)
                top_left[(i,j)] = top_left[(i-1, j-1)]
                if top_left[(i-1, j-1)] != None:
                    bot_right[top_left[(i-1, j-1)]] = (i,j)
        else:
            top_left[(i,j)] = None


def get_top_mid_and_bot_mid(arr, i, j):
    if (i,j) not in top_mid:
        if i-1 >= 0:
            if arr[i-1][j] != ".":
                top_mid[(i,j)] = (i-1, j)
                bot_mid[(i-1, j)] = (i,j)
            else:
                get_top_mid_and_bot_mid(arr, i-1, j)
                top_mid[(i,j)] = top_mid[(i-1, j)]
                if top_mid[(i-1, j)] != None:
                    bot_mid[top_mid[(i-1, j)]] = (i,j)
        else:
            top_mid[(i,j)] = None

def get_mid_left_and_mid_right(arr, i, j):
    if (i,j) not in mid_left:
        if j-1 >= 0:
            if arr[i][j-1] != ".":
                mid_left[(i,j)] = (i, j-1)
                mid_right[(i, j-1)] = (i,j)
            else:
                get_mid_left_and_mid_right(arr, i, j-1)
                mid_left[(i,j)] = mid_left[(i, j-1)]
                if mid_left[(i, j-1)] != None:
                    mid_right[mid_left[(i, j-1)]] = (i,j)
        else:
            mid_left[(i,j)] = None

def get_top_right_and_bot_left(arr, i, j):
    if (i,j) not in top_right:
        if i-1 >= 0 and j+1 < len(arr[0]):
            if arr[i-1][j+1] != ".":
                top_right[(i,j)] = (i-1, j+1)
                bot_left[(i-1, j+1)] = (i,j)
            else:
                get_top_right_and_bot_left(arr, i-1, j+1)
                top_right[(i,j)] = top_right[(i-1, j+1)]
                if top_right[(i-1, j+1)] != None:
                    bot_left[top_right[(i-1, j+1)]] = (i,j)
        else:
            top_right[(i,j)] = None



def get_occupied_count_new(arr, i, j):
    occupied_count = 0
    if (i,j) in top_left and top_left[(i,j)] != None and arr[top_left[(i,j)][0]][top_left[(i,j)][1]] == "#":
        occupied_count += 1
    if (i,j) in top_mid and top_mid[(i,j)] != None and arr[top_mid[(i,j)][0]][top_mid[(i,j)][1]] == "#":
        occupied_count += 1
    if (i,j) in top_right and top_right[(i,j)] != None and arr[top_right[(i,j)][0]][top_right[(i,j)][1]] == "#":
        occupied_count += 1
    if (i,j) in mid_left and mid_left[(i,j)] != None and arr[mid_left[(i,j)][0]][mid_left[(i,j)][1]] == "#":
        occupied_count += 1
    if (i,j) in mid_right and mid_right[(i,j)] != None and arr[mid_right[(i,j)][0]][mid_right[(i,j)][1]] == "#":
        occupied_count += 1
    if (i,j) in bot_left and bot_left[(i,j)] != None and arr[bot_left[(i,j)][0]][bot_left[(i,j)][1]] == "#":
        occupied_count += 1
    if (i,j) in bot_mid and bot_mid[(i,j)] != None and arr[bot_mid[(i,j)][0]][bot_mid[(i,j)][1]] == "#":
        occupied_count += 1
    if (i,j) in bot_right and bot_right[(i,j)] != None and arr[bot_right[(i,j)][0]][bot_right[(i,j)][1]] == "#":
        occupied_count += 1
    print("IK", i, j, occupied_count)
    return occupied_count


def mutate_new(arr):
    new_arr = []

    mutated = False
    occ = 0
    for i in range(len(arr)):
        curr_row = []
        for j in range(len(arr[0])):
            if arr[i][j] == ".":
                curr_row.append(".")
            elif arr[i][j] == "L":
                if get_occupied_count_new(arr, i, j) == 0:
                    curr_row.append("#")
                    occ += 1
                    mutated = True
                else:
                    curr_row.append("L")
            elif arr[i][j] == "#":
                if get_occupied_count_new(arr, i, j) >= 5:
                    curr_row.append("L")
                    mutated = True
                else:
                    occ += 1
                    curr_row.append("#")
        new_arr.append(curr_row)
    for j in range(len(new_arr)):
        print("".join(new_arr[j]))
    print("\n")
    return (mutated, new_arr, occ)

def part2():
    data_file = open("data.txt", "r")

    arr = []
    for line in data_file.readlines():
        row = [i for i in line.strip()]
        arr.append(row)
    

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != '.':
                get_top_left_and_bot_right(arr, i, j)
                get_top_mid_and_bot_mid(arr, i, j)
                get_mid_left_and_mid_right(arr, i, j)
                get_top_right_and_bot_left(arr, i, j)
                # print("IJ", i, j)
                # if (i,j) in top_left:
                #     print("top_left", top_left[(i,j)])
                # if (i,j) in bot_right:
                #     print("bot_right", bot_right[(i,j)])
                # if (i,j) in top_mid:
                #     print("top_mid", top_mid[(i,j)])
                # if (i,j) in bot_mid:
                #     print("bot_mid", bot_mid[(i,j)])
                # if (i,j) in mid_left:
                #     print("mid_left", mid_left[(i,j)])
                # if (i,j) in mid_right:
                #     print("mid_right", mid_right[(i,j)])
                # if (i,j) in top_right:
                #     print("top_right", top_right[(i,j)])
                # if (i,j) in bot_left:
                #     print("bot_left", bot_left[(i,j)])
                # print("\n")


    while True:
        mutated, new_arr, occ = mutate_new(arr)
        arr = new_arr
        if mutated == False:
            print(occ)
            break
    

part2()