# total = 0
# with open('day2-data.txt', 'r') as fp:
#     for line in fp:
#         count = 0
#         length = 0
#         width = 0
#         height = 0
#         for word in line.split("x"):
#             print("WORD")
#             if count == 0:
#                length = int(word)
#             if count == 1:
#                 width = int(word)
#             if count == 2:
#                 height = int(word)
#             count += 1
#         total += (2 * width * length) + (2 * width * height) + (2 * height * length)
#         total += min(width * length, (width * height), (height * length))
# print(total)


# total = 0
# with open('day2-data.txt', 'r') as fp:
#     for line in fp:
#         count = 0
#         length = 0
#         width = 0
#         height = 0
#         for word in line.split("x"):
#             # print("WORD")
#             if count == 0:
#                length = int(word)
#             if count == 1:
#                 width = int(word)
#             if count == 2:
#                 height = int(word)
#             count += 1
#         a = (2 * (width + length))
#         b = (2 * (width + height))
#         c = (2 * (height + length))
#         allMin = min(a, b, c)
#         bow = width * height * length
#         total += bow + allMin
# print(total)

