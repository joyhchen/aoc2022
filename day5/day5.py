def read_input():
    stacks = []
    instructions = []
    with open('day5.txt', "r") as f:
        for line in f:
            line_no_newline = line.rstrip('\n')
            if len(line_no_newline) > 0 and line_no_newline[0] != 'm':
                stacks.append(line_no_newline)
            elif len(line_no_newline) > 0:
                instructions.append(line_no_newline)
    return stacks[:-1], instructions

def parse_row(string_row):
    row_arr = []
    i = 0
    while i < len(string_row):
        cur_item = string_row[i:i+2].strip().replace('[', '')
        row_arr.append(cur_item)
        i+=4
    return row_arr

def parse_input():
    raw_stacks, raw_instructions = read_input()
    grid = []
    for string_row in raw_stacks:
        row_arr = parse_row(string_row)
        grid.append(row_arr)
    stacks = [[], [], [], [], [], [], [], [], []]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            item = grid[i][j]
            if len(item) > 0:
                stacks[j].append(item)

    instructions = []
    for ins in raw_instructions:
        # [num_to_move, from_col, to_col]
        no_words = ins.replace('move ', '').replace('from ', '').replace('to ', '')
        str_ints = no_words.split(' ')
        ints = map(lambda x: int(x), str_ints)
        instructions.append(list(ints))
    return stacks, instructions

def get_stacks_after_instruction(stacks, instruction):
    num_to_move = instruction[0]
    from_col = instruction[1] - 1
    to_col = instruction[2] - 1
    end_stacks = stacks
    i = 0

    while i < num_to_move:
        removed_item = stacks[from_col].pop(0)
        stacks[to_col].insert(0, removed_item)
        i+=1

    return end_stacks

def part1():
    stacks, instructions = parse_input()
    cur_stacks = stacks
    for instruction in instructions:
        cur_stacks = get_stacks_after_instruction(cur_stacks, instruction)

    top_of_stacks = map(lambda x: x[0], cur_stacks)
    return list(top_of_stacks)

def get_stacks_after_bulk_move(stacks, instruction):
    num_to_move = instruction[0]
    from_col = instruction[1] - 1
    to_col = instruction[2] - 1
    end_stacks = stacks
    i = 0

    ordered_list = []
    while i < num_to_move:
        removed_item = stacks[from_col].pop(0)
        ordered_list.append(removed_item)
        i+=1
    stacks[to_col] = ordered_list + stacks[to_col]
    return end_stacks

def part2():
    stacks, instructions = parse_input()
    cur_stacks = stacks
    for instruction in instructions:
        cur_stacks = get_stacks_after_bulk_move(cur_stacks, instruction)

    top_of_stacks = map(lambda x: x[0], cur_stacks)
    return list(top_of_stacks)

def main():
    result1 = part1()
    print(result1)
    result2 = part2()
    print(result2)

if __name__ == "__main__":
    main()
