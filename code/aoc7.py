from collections import defaultdict


if __name__ == "__main__":
    with open('inputs/input7.txt') as f:
        lines = f.readlines()
    
    # path_to_level_sum has full path as key, total file sizes at that level and below as value
    path_to_level_sum = defaultdict(int)

    is_listing = False
    counter = 0

    for line in lines:
        split_line = line.split()
        if split_line[0] == "$":
            if split_line[1] == "cd":
                if split_line[2] == "/":
                    current_path = "/"
                elif split_line[2] == "..":
                    current_path = "/".join(current_path.split("/")[:-1])
                else:
                    current_path += split_line[2] + "/"
            elif split_line[1] == "ls":
                continue
        elif split_line[0] == "dir":
            continue
        elif split_line[0].isnumeric():
            # Add total to current path as well as all parent paths
            current_path_split = current_path.split("/")
            for i in range(1, len(current_path_split)):
                path_to_level_sum["/".join(current_path_split[:i])] += int(split_line[0])

    sum = 0
    for path, level_sum in path_to_level_sum.items():
        if level_sum <= 100000:
            sum += level_sum
    print(sum)

    unused_space_needed = 30_000_000
    unused_space_had = 70_000_000 - path_to_level_sum[""]

    amount_to_delete = unused_space_needed - unused_space_had
    path_to_level_sum_tuples = sorted(path_to_level_sum.items(), key=lambda x: x[1], reverse=True)
    for tuple in path_to_level_sum_tuples:
        path, level_sum = tuple
        if level_sum > amount_to_delete:
            ans = level_sum
        else:
            break
    print(ans)
    


