import math

f = open("Data.txt")
lines = f.readlines()
s = 0
for line in lines:
    i = int(line.strip())
    s += math.floor(i/3) - 2
print(s)
