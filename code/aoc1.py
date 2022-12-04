import heapq


if __name__ == "__main__":
    with open('inputs/input1.txt') as f:
        lines = f.readlines()
    
    top_elves = []
    elf_count = 0
    for line in lines:
        if line == '\n':
            heapq.heappush(top_elves, -elf_count)
            elf_count = 0
        else:
            elf_count += int(line)
    print(-top_elves[0])
    s = 0
    s += heapq.heappop(top_elves)
    s += heapq.heappop(top_elves)
    s += heapq.heappop(top_elves)
    print(-s)