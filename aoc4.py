import requests
import heapq


if __name__ == "__main__":
    with open('input4.txt') as f:
        lines = f.readlines()

    contained_set_cnt = 0
    overlap_set_cnt = 0
    for line in lines:
        line = line.strip('\n')
        first, second = line.split(',')
        first_begin, first_end = first.split('-')
        second_begin, second_end = second.split('-')
        first_set = set(range(int(first_begin), int(first_end) + 1))
        second_set = set(range(int(second_begin), int(second_end) + 1))
        if (len(first_set - second_set) == (len(first_set) - len(second_set))) or (len(second_set - first_set) == (len(second_set) - len(first_set))):
            contained_set_cnt += 1
        if (len(first_set - second_set) < len(first_set) or (len(second_set - first_set) < len(second_set))):
            overlap_set_cnt += 1
    print(contained_set_cnt)
    print(overlap_set_cnt)

