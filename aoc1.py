import requests
import heapq


if __name__ == "__main__":
    with open('input1.txt') as f:
        lines = f.readlines()
    
    top_elves = []
    elf_count = 0
    max_elf_count = 0
    for line in lines:
        if line == '\n':
            max_elf_count = max(max_elf_count, elf_count)
            heapq.heappush(top_elves, -elf_count)
            elf_count = 0
        else:
            elf_count += int(line)

    
    print(max_elf_count)
    s = 0
    s += heapq.heappop(top_elves)
    s += heapq.heappop(top_elves)
    s += heapq.heappop(top_elves)
    print(s)