import time
import re
import itertools


def part1(input_file):
    memory = {}

    for row in input_file:
        if row[0] == "mask":
            mask = row[1]
            X = [x for x, _ in enumerate(mask) if _ == "X"]
        else:
            mem_location = re.search(r'\[(.*?)\]', row[0]).group(1)
            binary = '{:036b}'.format(int(row[1]))
            masked_result = "".join(
                [bit if j not in X else binary[j] for j, bit in enumerate(mask)])
            memory[mem_location] = int(masked_result, 2)

    return sum(memory.values())


def part2(input_file):
    memory = {}

    for row in input_file:
        if row[0] == "mask":
            mask = row[1]
            X = [x for x, _ in enumerate(mask) if _ == "X"]
        else:
            mem_location = re.search(r'\[(.*?)\]', row[0]).group(1)
            binary = '{:036b}'.format(int(mem_location))
            temp_binary = []
            for add_bit, bitmask in zip(binary, mask):
                if bitmask == "0":
                    temp_binary.append(add_bit)
                elif bitmask == "1":
                    temp_binary.append("1")
                else:
                    temp_binary.append("X")
            temp_binary = "".join(temp_binary)
            for combo in itertools.combinations([0, 1] * len(X), len(X)):
                for i, x in enumerate(X):
                    temp_binary = temp_binary[:x] + \
                        str(combo[i]) + temp_binary[x+1:]
                memory[int(temp_binary, 2)] = int(row[1])

    return sum(memory.values())


if __name__ == "__main__":
    with open("../input/day14.txt") as f:
        input_file = f.read().splitlines()

    input_file = [f.split(" = ") for f in input_file]

    start = time.time()
    part1_result = part1(input_file)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1 answer: {part1_result}. Took: {elapsed} seconds.")

    start = time.time()
    part2_result = part2(input_file)
    elapsed = round(time.time() - start, 3)
    print(f"Part 2 answer: {part2_result}. Took: {elapsed} seconds.")
