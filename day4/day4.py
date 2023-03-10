def read_pairs():
    lines = []
    with open('day4.txt', "r") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def parse_pair(pairs_string):
    pairs_strings_arr = pairs_string.split(',')

    int_pairs = []
    for pair_str in pairs_strings_arr:
        lower_upper_str = pair_str.split('-')
        lower_upper = map(lambda x: int(x), lower_upper_str)
        int_pairs.append(list(lower_upper))
    return int_pairs

def fully_contained(a1, a2):
    # example: a1 = [20, 30] and a2 = [21, 29]
    # example: a1 = [21, 29] and a2 = [20, 30]
    a1_contains_a2 = (a1[0] <= a2[0]) and (a1[1] >= a2[1])
    a2_contains_a1 = (a2[0] <= a1[0]) and (a2[1] >= a1[1])
    return a1_contains_a2 or a2_contains_a1

def overlap(a1, a2):
    a1_overlaps_a2 = (a1[1] >= a2[0]) and (a1[0] <= a2[1])
    a2_overlaps_a1 = (a2[1] >= a1[0]) and (a2[0] <= a1[1])
    return a1_overlaps_a2 or a2_overlaps_a1

def solve(function_to_evaluate):
    pairs = read_pairs()
    total_sum = 0
    for str_pair in pairs:
        pair = parse_pair(str_pair)
        condition_met = function_to_evaluate(pair[0], pair[1])
        if condition_met:
            total_sum += 1
    return total_sum

def main():
    result1 = solve(fully_contained)
    print(result1)
    result2 = solve(overlap)
    print(result2)

if __name__ == "__main__":
    main()
