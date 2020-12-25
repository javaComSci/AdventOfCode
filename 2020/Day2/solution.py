from collections import Counter

def part1():
    data_file = open("data.txt", "r")

    valid = 0

    for line in data_file.readlines():
        count, letter, pwd = line.split()
        count_split = count.split("-")
        min_count = int(count_split[0])
        max_count = int(count_split[1])
        letter = letter[0]
        
        counts_in_letter = Counter(pwd)
        if counts_in_letter[letter] >= min_count and counts_in_letter[letter] <= max_count:
            valid += 1

    print(valid)


def part2():
    data_file = open("data.txt", "r")

    valid = 0

    for line in data_file.readlines():
        count, letter, pwd = line.split()
        count_split = count.split("-")
        l_index = int(count_split[0])
        r_index = int(count_split[1])
        letter = letter[0]
        
        if pwd[l_index - 1] == letter and pwd[r_index - 1] != letter:
            valid += 1
        if pwd[l_index - 1] != letter and pwd[r_index - 1] == letter:
                valid +=1
    print(valid)


part2()