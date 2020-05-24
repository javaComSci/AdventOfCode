# PART 1
# f = open("Data.txt")
# lines = f.readlines()
# lines.sort()

# length = len(lines)
# # length = 3

# guardDuty = 0
# sleepStart = 0
# sleepEnd = 0
# sleepTimes = {}

# for i in range(length):
#     line = lines[i].strip()
#     lineSplit = line.split(" ")
#     print(lineSplit)

#     # new guard on duty
#     if lineSplit[2] == "Guard":
#         guardDuty = int(lineSplit[3][1:])
#         # print("DUTY IS " + str(guardDuty))
#     elif lineSplit[2] == "falls":
#         sleepStart = int(lineSplit[1][3:-1])
#         # print("SLEEP START IS " + str(sleepStart))
#     else:
#         sleepEnd = int(lineSplit[1][3:-1])
#         # print("SLEEP END IS " + str(sleepEnd))
#         newSleepTimes = [1 if j >= sleepStart and j < sleepEnd else 0 for j in range(60)]
#         print(newSleepTimes)
#         if guardDuty in sleepTimes:
#             sleepTimes[guardDuty] = [x + y for x, y in zip(sleepTimes[guardDuty], newSleepTimes)]
#         else:
#             sleepTimes[guardDuty] = newSleepTimes
# print(sleepTimes)

# maxTime = 0
# bestIndex = 0
# bestGuard = 0
# for guard in sleepTimes:
#     maxTime = max(sum(sleepTimes[guard]), maxTime)
#     if maxTime == sum(sleepTimes[guard]):
#         values = sleepTimes[guard]
#         bestIndex = values.index(max(values))
#         bestGuard = guard
#         print(bestIndex, bestGuard)
# print(bestIndex * bestGuard)







# PART 2
import collections

f = open("Data.txt")
lines = f.readlines()
lines.sort()

length = len(lines)

guardDuty = 0
sleepStart = 0
sleepEnd = 0
sleepTimes = {}

for i in range(length):
    line = lines[i].strip()
    lineSplit = line.split(" ")
    print(lineSplit)

    # new guard on duty
    if lineSplit[2] == "Guard":
        guardDuty = int(lineSplit[3][1:])
        # print("DUTY IS " + str(guardDuty))
    elif lineSplit[2] == "falls":
        sleepStart = int(lineSplit[1][3:-1])
        # print("SLEEP START IS " + str(sleepStart))
    else:
        sleepEnd = int(lineSplit[1][3:-1])
        # print("SLEEP END IS " + str(sleepEnd))
        for j in range(60):
            if j >= sleepStart and j < sleepEnd:
                if j in sleepTimes:
                    sleepTimes[j].append(guardDuty)
                else:
                    sleepTimes[j] = [guardDuty]
print(sleepTimes)

bestMin = 0
maxElems = 0
m = None
for minute in sleepTimes:
    c = collections.Counter(sleepTimes[minute])
    mostCom, numCom = c.most_common(1)[0]
    if numCom >= maxElems:
        bestMin = mostCom
        maxElems = numCom
        m = minute
print(bestMin, maxElems, m)
print(m * bestMin)