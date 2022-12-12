from collections import deque


if __name__ == "__main__":
    with open('inputs/input6.txt') as f:
        lines = f.readlines()
    recent_input = deque()
    recent_input_2 = deque()
    recent_input_start_char = 0
    ans1 = -1
    ans2 = -1
    for line in lines:
        char_list = list(line)
        for char in char_list:
            recent_input_start_char += 1
            if len(set(recent_input)) == 4:
                ans1 = recent_input_start_char-1
            if len(set(recent_input_2)) == 14:
                ans2 = recent_input_start_char-1
            if ans1 == -1 and recent_input and len(recent_input) == 4:
                recent_input.popleft()
            if ans2 == -1 and recent_input_2 and len(recent_input_2) == 14:
                recent_input_2.popleft()
            recent_input.append(char)
            recent_input_2.append(char)
    print("EOM", ans1)
    print("SOM", ans2)


