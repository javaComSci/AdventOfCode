# count = 0
# with open("day1-1-data.txt","r") as f:
#     while True:
#         c = f.read(1)
#         if not c:
#             break
#         if c == '(':
#             count += 1
#         else:
#             count -= 1

# print(count)


count = 0
floors = 0
with open("day1-1-data.txt","r") as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if c == '(':
            count += 1
        else:
            count -= 1
        if count == -1:
            break
        floors += 1

print(floors + 1)