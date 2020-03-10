# i = 0
# j = 0
# s = {(0,0)}
# with open("day3-data.txt","r") as f:
#     while True:
#         c = f.read(1)
#         if not c:
#             break
#         # print(c)
#         if c == '>':
#             j += 1
#         elif c == '<':
#             j -= 1
#         elif c == '^':
#             i -= 1
#         elif c == 'v':
#             i +=1
#         s.add((i, j))
# # print(s)
# print(len(s))
        

i1 = 0
j1 = 0
i2 = 0
j2 = 0
turn = 0
s = {(0,0)}
with open("day3-data.txt","r") as f:
    while True:
        c = f.read(1)
        if not c:
            break
        # print(c)
        if c == '>':
            if turn == 0:
                j1 += 1
            else:
                j2 += 1
        elif c == '<':
            if turn == 0:
                j1 -= 1
            else:
                j2 -= 1
        elif c == '^':
            if turn == 0:
                i1 += 1
            else:
                i2 += 1
        elif c == 'v':
            if turn == 0:
                i1 -= 1
            else:
                i2 -= 1
        if turn == 0:
            s.add((i1, j1))
        else:
            s.add((i2, j2))
        turn = (turn + 1) %2
# print(s)
print(len(s))