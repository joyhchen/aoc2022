def read_rucksacks():
    lines = []
    with open('day3.txt', "r") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def find_rucksack_compartments_common_item(rucksack):
    rucksack_split = int(len(rucksack) / 2)
    comp1 = rucksack[:rucksack_split]
    comp2 = rucksack[rucksack_split:]
    comp1_set = set(comp1)
    for item in comp2:
        if item in comp1_set:
            return item

def map_item_to_priority(item):
    if (item.islower()):
        return ord(item) - 96
    else:
        return ord(item) - 38

def part1():
    rucksacks = read_rucksacks()
    sum = 0
    for rucksack in rucksacks:
        common_item = find_rucksack_compartments_common_item(rucksack)
        priority = map_item_to_priority(common_item)
        sum += priority
    print(sum)

def find_group_common_item(group):
    rucksack1 = set(group[0])
    rucksack2 = set(group[1])
    rucksack3 = set(group[2])
    intersection = rucksack1.intersection(rucksack2).intersection(rucksack3)
    common_item = list(intersection)[0]
    return common_item

def get_rucksack_groups(rucksacks):
    i = 0
    groups = []
    while i < len(rucksacks):
        group = [rucksacks[i], rucksacks[i+1], rucksacks[i+2]]
        groups.append(group)
        i+=3
    return groups

def part2():
    rucksacks = read_rucksacks()
    groups = get_rucksack_groups(rucksacks)
    sum = 0
    for group in groups:
        common_item = find_group_common_item(group)
        priority = map_item_to_priority(common_item)
        sum += priority
    print(sum)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
