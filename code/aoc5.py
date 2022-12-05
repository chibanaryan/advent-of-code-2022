from collections import deque


if __name__ == "__main__":
    with open('inputs/input5.txt') as f:
        lines = f.readlines()

    stacks = [deque([]) for _ in range(9)]
    stacks_part2 = [deque([]) for _ in range(9)]
    setup_time = True

    for line in lines:
        if setup_time:
            for idx, char in enumerate(line):
                if char.isalpha():
                    stack_idx = (idx - 1) // 4
                    stacks[stack_idx].appendleft(char)
                    stacks_part2[stack_idx].appendleft(char)

        if line == '\n':
            setup_time = False

        if not setup_time:
            splt = line.split()
            if len(splt) > 0 and splt[0] == 'move':
                quantity, source, destination = int(splt[1]), int(splt[3]), int(splt[5])
                moved_stack_part2 = deque()
                for x in range(quantity):
                    if len(stacks[source-1]) > 0:
                        stacks[destination-1].append(stacks[source-1].pop())
                    if len(stacks_part2[source-1]) > 0:
                        moved_stack_part2.appendleft(stacks_part2[source-1].pop())
                while moved_stack_part2:
                    stacks_part2[destination-1].append(moved_stack_part2.popleft())

    ans = []
    ans_part2 = []

    for stack in stacks:
        if len(stack) > 0:
            ans.append((stack.pop()))

    for stack in stacks_part2:
        if len(stack) > 0:
            ans_part2.append((stack.pop()))

    print(''.join(ans))
    print(''.join(ans_part2))