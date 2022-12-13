from collections import defaultdict


if __name__ == "__main__":
    with open('inputs/input8.txt') as f:
        lines = f.readlines()
    tree_coords_visible = set()

    # Visibility from left & right
    for line_idx in range(len(lines)):
        max_in_line_from_left = -1
        for idx in range(len(lines[0])):
            char = lines[line_idx][idx]
            if char.isnumeric():
                height = int(char)
                if height > max_in_line_from_left:
                    tree_coords_visible.add((idx, line_idx))
                    max_in_line_from_left = height
        max_in_line_from_right = -1
        for idx in range(len(lines[0])-1, -1, -1):
            char = lines[line_idx][idx]
            if char.isnumeric():
                height = int(char)
                if height > max_in_line_from_right:
                    tree_coords_visible.add((idx, line_idx))
                    max_in_line_from_right = height
    
    # Visibility from top and bottom
    for idx in range(len(lines[0])):
        max_in_line_from_top = -1
        for line_idx in range(len(lines)):
            char = lines[line_idx][idx]
            if char.isnumeric():
                height = int(char)
                if height > max_in_line_from_top:
                    tree_coords_visible.add((idx, line_idx))
                    max_in_line_from_top = height
        max_in_line_from_bottom = -1
        for line_idx in range(len(lines)-1, -1, -1):
            char = lines[line_idx][idx]
            if char.isnumeric():
                height = int(char)
                if height > max_in_line_from_bottom:
                    tree_coords_visible.add((idx, line_idx))
                    max_in_line_from_bottom = height
    print(tree_coords_visible)
    print(len(tree_coords_visible))
    # print(len(lines[0]))
    # print(len(lines))
