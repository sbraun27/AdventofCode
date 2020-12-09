import time
import itertools


def part1(input_list, start_number):
    for idx, target in enumerate(input_list[start_number:]):
        preceeding_list = input_list[idx:idx+start_number]
        in_list = False
        for i, j in itertools.combinations(preceeding_list, 2):
            if i + j == target:
                in_list = True
                break

        if not in_list:
            return target


def part2(input_list, target):
    # Determine the current set length
    for i in range(2, len(input_list)):
        # Determine the starting index
        for j in range(len(input_list) - i):
            target_set = input_list[j:j+i]
            if sum(target_set) == target:
                minimum = min(target_set)
                maximum = max(target_set)
                return minimum + maximum


if __name__ == "__main__":
    with open("../input/day9.txt", "r") as f:
        input_list = f.read().splitlines()

    input_list = [int(i) for i in input_list]
    start = time.time()
    part1_answer = part1(input_list, 25)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1 Result: {part1_answer}. Took: {elapsed}.")

    start = time.time()
    part2_answer = part2(input_list, part1_answer)
    elapsed = round(time.time() - start, 3)
    print(f"Part 2 Result: {part2_answer}. Took: {elapsed}.")
