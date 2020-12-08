import time
import copy


def parse_to_list(input_file):
    rules = []
    for line in input_file:
        split_line = line.split()
        rules.append([split_line[0], int(split_line[1]), 0])
        # [command, value, completed
    return rules


def part1(rules):
    i = 0
    acc = 0
    completed_idx = set()

    while i not in completed_idx and i < len(rules):
        completed_idx.add(i)
        current = rules[i]
        if current[0] == "jmp":
            i += current[1]
            continue
        if current[0] == "acc":
            acc += current[1]

        i += 1

    return (i < len(rules)), acc


def part2(rules):
    for i, current in enumerate(rules):
        if current[0] == "acc":
            continue

        if current[0] == "nop":
            adjusted_operation = "jmp"
        else:
            adjusted_operation = "nop"

        test_rules = copy.deepcopy(rules)
        test_rules[i][0] = adjusted_operation
        has_inf_loop, acc = part1(test_rules)

        if not has_inf_loop:
            return acc


if __name__ == "__main__":
    with open("../input/day8.txt", "r") as f:
        input_file = f.read().splitlines()

    rules = parse_to_list(input_file)
    start = time.time()
    infinite_loop, acc = part1(rules.copy())
    elapsed = round(time.time() - start, 3)
    print(f"Part 1 result: {acc}. Took: {elapsed} seconds.")

    start = time.time()
    part2 = part2(rules)
    elapsed = round(time.time() - start, 3)
    print(f"Part 2 result: {part2}. Took: {elapsed} seconds.")
