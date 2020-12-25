# PART 1
def part1():
    data_file = open("data.txt", "r")

    nums = []

    for line in data_file.readlines():
        num = int(line.strip())
        nums.append(num)

    nums.sort()

    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < 2020:
            left += 1
        elif nums[left] + nums[right] > 2020:
            right -= 1
        else:
            print(nums[left] * nums[right])
            break



# PART 2
def part2():
    data_file = open("data.txt", "r")

    nums = []

    for line in data_file.readlines():
        num = int(line.strip())
        nums.append(num)

    nums.sort()

    for i in range(len(nums)):
        nums_copy = nums[:i] + nums[i+1:]

        num_needed = 2020 - nums[i]

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] < num_needed:
                left += 1
            elif nums[left] + nums[right] > num_needed:
                right -= 1
            else:
                print(nums[left] * nums[right] * nums[i])
                break


part2()