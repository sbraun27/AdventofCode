import time


def part1(input_file):
    return sum([int(i)//3 - 2 for i in input_file])


def part2(input_file):
    results = 0
    for module in input_file:
        fuel = int(module)//3 - 2
        results += fuel
        fuel_needed = fuel // 3 - 2
        while True:
            if fuel_needed <= 0:
                break
            else:
                results += fuel_needed
                fuel_needed = fuel_needed // 3 - 2

    return results


if __name__ == "__main__":
    with open("../input/day1.txt") as f:
        input_file = f.read().splitlines()

    start = time.time()
    part1_result = part1(input_file)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1 result: {part1_result}. Took: {elapsed} seconds.")

    start = time.time()
    part2_result = part2(input_file)
    elapsed = round(time.time() - start, 3)
    print(f"Part 2 result: {part2_result}. Took: {elapsed} seconds.")
