# PART 1
# import re
# f = open("Data.txt")
# lines = f.readlines()
# occupied = set()
# count = set() 
# for line in lines:
#     splitArr = line.replace(" ", "")
#     splitArr = re.split("@|x|,|:|\n", splitArr)
#     print(splitArr)
#     startCol = int(splitArr[1])
#     startRow = int(splitArr[2])
#     width = int(splitArr[3])
#     height = int(splitArr[4])
#     for w in range(startCol, startCol + width):
#         for h in range(startRow, startRow + height):
#             if (w, h) in occupied:
#                 count.add((w, h))
#             else:
#                 occupied.add((w, h))
# print(len(count))


import re
f = open("Data.txt")
lines = f.readlines()
occupied = {}
for line in lines:
    splitArr = line.replace(" ", "")
    splitArr = re.split("@|x|,|:|\n", splitArr)
    startCol = int(splitArr[1])
    startRow = int(splitArr[2])
    width = int(splitArr[3])
    height = int(splitArr[4])
    for w in range(startCol, startCol + width):
        for h in range(startRow, startRow + height):
            if (w, h) in occupied:
                occupied[(w, h)] = "X"
            else:
                occupied[(w, h)] = splitArr[0]
for line in lines:
    splitArr = line.replace(" ", "")
    splitArr = re.split("@|x|,|:|\n", splitArr)
    startCol = int(splitArr[1])
    startRow = int(splitArr[2])
    width = int(splitArr[3])
    height = int(splitArr[4])
    found = False
    for w in range(startCol, startCol + width):
        for h in range(startRow, startRow + height):
            if (w, h) in occupied and occupied[(w, h)] == "X":
                found = True

    if found == False:
        print(line)
    
