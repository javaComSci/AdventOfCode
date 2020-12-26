def part1():
    data_file = open("data.txt", "r")

    acc_val = 0
    instructions = []
    for line in data_file.readlines():
        values = line.strip().split()
        instruction = values[0]
        move_dir = values[1][0]
        operand = values[1][1:]
        instructions.append((instruction, move_dir, int(operand)))
    
    print(instructions)

    seen_instructions = set()
    instruction_curr = 0
    while instruction_curr not in seen_instructions:
        seen_instructions.add(instruction_curr)
        instruction = instructions[instruction_curr]
        if instruction[0] == "nop":
            instruction_curr += 1
        elif instruction[0] == "acc":
            if instruction[1] == "+":
                acc_val += instruction[2]
            else:
                 acc_val -= instruction[2]
            instruction_curr += 1
        else:
            if instruction[1] == "+":
                instruction_curr += instruction[2]
            else:
                instruction_curr -= instruction[2]
    print(acc_val)


def check_loop(instructions):
    seen_instructions = set()
    instruction_curr = 0
    acc_val = 0
    while True:
        if instruction_curr == len(instructions):
            return (True, acc_val)
        if instruction_curr in seen_instructions:
            return (False, 0)
        seen_instructions.add(instruction_curr)
        instruction = instructions[instruction_curr]
        if instruction[0] == "nop":
            instruction_curr += 1
        elif instruction[0] == "acc":
            if instruction[1] == "+":
                acc_val += instruction[2]
            else:
                 acc_val -= instruction[2]
            instruction_curr += 1
        else:
            if instruction[1] == "+":
                instruction_curr += instruction[2]
            else:
                instruction_curr -= instruction[2]
    return (True, acc_val)
    

def do_change(instructions):
    for i in instructions:
        if i[0] == "jmp":
            i[0] = "nop"
            b, val = check_loop(instructions)
            if b == True:
                print(instructions)
                return val
            else:
                i[0] = "jmp"
        elif i[0] == "nop":
            i[0] = "jmp"
            b, val = check_loop(instructions)
            if b == True:
                print(instructions)
                return val
            else:
                i[0] = "nop"
        else:
            continue

def part2():
    data_file = open("data.txt", "r")

    
    instructions = []
    for line in data_file.readlines():
        values = line.strip().split()
        instruction = values[0]
        move_dir = values[1][0]
        operand = values[1][1:]
        instructions.append([instruction, move_dir, int(operand)])

    changed_val = do_change(instructions)
    print(changed_val)



part2()