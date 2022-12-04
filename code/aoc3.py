def char_to_priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 27


if __name__ == "__main__":
    with open('inputs/input3.txt') as f:
        lines = f.readlines()
    
    priority_sum = 0
    group_sum = 0
    groups = []
    for line in lines:
        line = line.strip('\n')
        half = len(line) // 2
        first_half = line[:half]
        second_half = line[half:]
        first_set = set(first_half)
        second_set = set(second_half)
        unique_char = first_set.intersection(second_set).pop()
        priority_sum += char_to_priority(unique_char)
        groups.append(set(line))
        if len(groups) == 3:
            common_char = groups[0].intersection(groups[1], groups[2]).pop()
            group_sum += char_to_priority(common_char)
            groups = []
    print(priority_sum)
    print(group_sum)

