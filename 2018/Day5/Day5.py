# Part 1
# f = open("Data.txt")
# pol = f.readline().strip()

# i = 0
# count = 0
# while i < len(pol) - 1:
#     # same letter so can do checking
#     if pol[i].upper() == pol[i + 1].upper() and ((pol[i].isupper() and pol[i + 1].islower()) or (pol[i].islower() and pol[i + 1].isupper())):
#         pol = pol[:i] + pol[i + 2:]
#         if i > 0:
#             i = i - 1
#         else:
#             i = 0
#     else:
#         i += 1
#     print(i, pol[i])
#     count += 1
#     print("COUNT ", count)
# print(pol)
# print(len(pol))




# Part 2
import math

def collapse(pol):
    i = 0
    count = 0
    while i < len(pol) - 1:
        # same letter so can do checking
        if pol[i].upper() == pol[i + 1].upper() and ((pol[i].isupper() and pol[i + 1].islower()) or (pol[i].islower() and pol[i + 1].isupper())):
            pol = pol[:i] + pol[i + 2:]
            if i > 0:
                i = i - 1
            else:
                i = 0
        else:
            i += 1
    return len(pol)

f = open("Data.txt")
pol = f.readline().strip()

letters = set()
for letter in pol:
    letters.add(letter.upper())
letters = list(letters)

shortest = math.inf
for letter in letters:
    newPol = pol
    newPol = newPol.replace(letter.upper(), '')
    newPol = newPol.replace(letter.lower(), '')
    print("NEW POL REMOVED ", letter, newPol)
    length = collapse(newPol)
    shortest = min(length, shortest)

print(shortest)

