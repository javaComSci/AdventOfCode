# PART 1
def part1():
    data_file = open("data.txt", "r")

    tree_map = []

    for line in data_file.readlines():
        l = [str(l) for l in line.strip()]
        tree_map.append(l)

    col = 3
    trees = 0
    for row in range(1, len(tree_map)):
        c = col
        if c >= len(tree_map[0]):
            c = col % len(tree_map[0])
        print(tree_map[row][c])
        if tree_map[row][c] == "#":
            trees += 1
        col += 3
    
    print(trees)


# PART 2
def get_tree_info(right, down):
    data_file = open("data.txt", "r")

    tree_map = []

    for line in data_file.readlines():
        l = [str(l) for l in line.strip()]
        tree_map.append(l)

    col = right
    trees = 0
    for row in range(down, len(tree_map), down):
        c = col
        if c >= len(tree_map[0]):
            c = col % len(tree_map[0])
        if tree_map[row][c] == "#":
            trees += 1
        col += right
    
    print(trees)
    return trees


def part2():
    print(get_tree_info(1, 1) * get_tree_info(3, 1) * get_tree_info(5, 1) * get_tree_info(7, 1) * get_tree_info(1, 2))

part2()