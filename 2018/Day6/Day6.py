f = open("Data.txt", "r")
allCoordinates = []
maxX = 0
maxY = 0

for line in f:
    coordinates = line.strip().split(",")
    allCoordinates.append([int(coordinates[0]), int(coordinates[1])])
    maxX = max(maxX, int(coordinates[0]))
    maxY = max(maxY, int(coordinates[1]))

print(allCoordinates)
print(maxX)
print(maxY)

matrix = [[0 for y in range(maxY + 1)] for x in range(maxX + 1)]

