# PART 1
# f = open("data.txt")
# lines = f.readlines()
# s = 0
# for line in lines:
#     cutline = line.strip()
#     if cutline[0] == "+":
#         s = s + int(cutline[1:])
#     else:
#         s = s - int(cutline[1:])
# print(s)




# PART 2
f = open("data.txt")
lines = f.readlines()

seenSet = set()
seenSet.add(0)
currSum = 0
foundVal = False
while True:
    for line in lines:
        firstTime = True
        cutline = line.strip()
        if cutline[0] == "+":
            currSum += int(cutline[1:])
        else:
            currSum -= int(cutline[1:])
        
        if currSum in seenSet:
            print(currSum)
            foundVal = True
            break
        seenSet.add(currSum)
        # print("SEEN ", currSum)
        # print("SEEN SET ", seenSet)
        
    if foundVal == True:
        break