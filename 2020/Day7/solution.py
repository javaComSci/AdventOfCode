def get_parents(vertex_list, current, to_explore, explored):
    explored.add(current)
    to_explore.remove(current)
    for parent in vertex_list:
        if current in vertex_list[parent] and parent not in explored:
            to_explore.add(parent)
            get_parents(vertex_list, parent, to_explore, explored)
    


def part1():
    data_file = open("data.txt", "r")

    vertex_list = {}

    for line in data_file.readlines():
        # create a graph such that each bag is a node and have connections
        # represent as an vertex list
        l = line.strip().split()
        parent_bag = " ".join(l[:2])
        other_bags = [i.strip() for i in " ".join(l[4:]).split(",")]
        if other_bags[0] == "no other bags.":
            vertex_list[parent_bag] = []
        else:
            other_bag_list = []
            for bag in other_bags:
                new_bag = " ".join(bag.split()[1:-1])
                other_bag_list.append(new_bag)
            vertex_list[parent_bag] = other_bag_list
    

    print(vertex_list)
    to_explore = {"shiny gold"}
    explored = set()
    get_parents(vertex_list, "shiny gold", to_explore, explored)
    print(len(explored) - 1)
    


def get_child_bags(vertex_list, vertex_list_nums, current):
    print("CALLING FOR", current)
    children = vertex_list[current]
    children_nums = vertex_list_nums[current]
    total = 1
    for i in range(len(children)):
        child = children[i]
        child_val = children_nums[i]
        print("PARENT", current, "CHILD", child)
        num = get_child_bags(vertex_list, vertex_list_nums, child)
        total += num * child_val
    print("CALLED DONE FOR", current, total)
    return total

def part2():
    data_file = open("data.txt", "r")

    vertex_list = {}
    vertex_list_nums = {}

    for line in data_file.readlines():
        # create a graph such that each bag is a node and have connections
        # represent as an vertex list
        # start from the shiny and go down to see 
        l = line.strip().split()
        parent_bag = " ".join(l[:2])
        other_bags = [i.strip() for i in " ".join(l[4:]).split(",")]
        if other_bags[0] == "no other bags.":
            vertex_list[parent_bag] = []
            vertex_list_nums[parent_bag] = [0]
        else:
            other_bag_list = []
            value_bag_list = []
            for bag in other_bags:
                new_bag = " ".join(bag.split()[1:-1])
                other_bag_list.append(new_bag)
                value_bag_list.append(int(bag.split()[0]))
            vertex_list[parent_bag] = other_bag_list
            vertex_list_nums[parent_bag] = value_bag_list
    print(vertex_list)
    print(vertex_list_nums)

    total = get_child_bags(vertex_list, vertex_list_nums, "shiny gold")
    print("TOTAL",total)


part2()