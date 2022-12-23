import collections

def read_input():
    lines = []
    with open('day6.txt', "r") as f:
        for line in f:
            lines.append(line)
    return lines[0]

def find_signal(buffer, window_len):
    cur_window = list(buffer[:window_len])
    cur_dict = collections.defaultdict(int)
    for el in cur_window:
        cur_dict[el]+=1

    unique_els = len(cur_dict)

    i = window_len
    while i < len(buffer):
        removed_item = cur_window.pop(0)
        cur_dict[removed_item] -= 1
        if cur_dict[removed_item] <= 0:
            unique_els -= 1

        new_item = buffer[i]
        cur_window.append(new_item)
        num_new_item = cur_dict[new_item]
        if num_new_item <= 0:
            unique_els+=1
        cur_dict[new_item] += 1
        if unique_els == window_len:
            # found it
            return i + 1
        i+=1

def main():
    buffer = read_input()
    part1_signal = find_signal(buffer, 4)
    print(part1_signal)
    part2_signal = find_signal(buffer, 14)
    print(part2_signal)

if __name__ == "__main__":
    main()
