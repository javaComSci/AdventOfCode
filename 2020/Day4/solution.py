# PART 1

def check_passport(pst):
    print(pst)
    if len(pst["byr"]) != 4 or int(pst["byr"]) < 1920 or int(pst["byr"]) > 2002:
        print(1)
        return False    
    if len(pst["iyr"]) != 4 or int(pst["iyr"]) < 2010 or int(pst["iyr"]) > 2020:
        print(2)
        return False
    if len(pst["eyr"]) != 4 or int(pst["eyr"]) < 2020 or int(pst["eyr"]) > 2030:
        print(3)
        return False

    if len(pst["pid"]) != 9:
        print(4)
        return False

    ecl = pst["ecl"]
    if ecl not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        print(5)
        return False
    
    hcl = pst["hcl"]
    if hcl[0] != "#":
        print(6)
        return False
    if len(hcl) != 7:
        print(7)
        return False
    for h in hcl[1:]:
        if h.isdigit():
            continue
        if h.isalpha() and h <= "f":
            continue
        return False
    
    hgt = pst["hgt"]
    if len(hgt) < 3:
        print(8)
        return False
    if hgt[len(hgt) - 2:] == "cm":
        l = int(hgt[:-2])
        print(l)
        if (l >= 150 and l <= 193)== False:
            print(8)
            return False
    elif hgt[len(hgt) - 2:] == "in":
        l = int(hgt[:-2])
        if (l >= 59 and l <= 76)== False:
            print(9)
            return False

    return True


def part1():
    data_file = open("data.txt", "r")

    passport_info = []
    temp = {}
    valid = 0
    req = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for line in data_file.readlines():
        l = line.strip().split()
        if len(l) != 0:
            for i in range(len(l)):
                key, val = l[i].split(":")
                temp[key] = val
        if len(l) == 0:
            if req.issubset(set(temp.keys())) and check_passport(temp):
                valid += 1
            temp = {}

    if req.issubset(set(temp.keys())) and check_passport(temp):
                valid += 1

    print(valid)
            

part1()