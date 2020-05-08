# PART 1
# from collections import Counter

# f = open("Data.txt")
# lines = f.readlines()
# haveThree = 0
# haveTwo = 0
# for line in lines:
#     res = Counter(line)
#     if 3 in res.values():
#         haveThree += 1
#     if 2 in res.values():
#         haveTwo += 1
# print(haveThree * haveTwo)


# PART 2
f = open("Data.txt")
lines = f.readlines()

for l1 in lines:
    for l2 in lines:
        c = 0
        pos = 0
        for i in range(len(l1) - 1):
            if l1[i] != l2[i]:
                c += 1
                pos = i
        if c == 1:
            s = l1[:pos] + l1[pos + 1:]
            print(s)
            exit()
