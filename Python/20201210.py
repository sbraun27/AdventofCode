import time


def part1(input_file, current_jolt=0):
    input_file.sort()

    jolt1 = 0
    jolt2 = 0
    jolt3 = 0

    for adapter in input_file:
        current_diff = adapter - current_jolt
        if current_diff == 1:
            jolt1 += 1
        elif current_diff == 2:
            jolt2 += 1
        elif current_diff == 3:
            jolt3 += 1
        else:
            # This would mean either a 0 difference or greater than 3. pass for now
            pass
        current_jolt = adapter

    jolt3 += 1
    return jolt1 * jolt3


def part2(input_file, current_jolt=0):
    num_path_adapters = {
        0: 1
    }

    for adapter in input_file:
        num_path_adapters[adapter] = 0
        for possible_adapter in range(adapter-3, adapter):
            if possible_adapter == 0 or possible_adapter in input_file:
                num_path_adapters[adapter] += num_path_adapters[possible_adapter]

    return num_path_adapters[input_file[-1]]


if __name__ == "__main__":
    with open("../input/day10.txt", "r") as f:
        input_file = f.read().splitlines()

    input_file = [int(i) for i in input_file]

    part1_answer = part1(input_file)
    print(part1_answer)

    part2_answer = part2(input_file)
    print(part2_answer)
