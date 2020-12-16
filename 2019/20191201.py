import time


def part1(input_file):
    fuel = [int(i)//3 - 2 for i in input_file]

    return sum(fuel)


def part2(input_file):
    results = []
    for module in input_file:
        fuel = [int(module)//3-2]
        while True:
            required_fuel = fuel[-1]//3-2
            if required_fuel <= 0:
                break
            else:
                fuel.append(required_fuel)
        results.append(sum(fuel))

    return sum(results)


if __name__ == "__main__":
    with open("day1.txt") as f:
        input_file = f.read().splitlines()

    start = time.time()
    part1_result = part1(input_file)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1 result: {part1_result}. Took: {elapsed} seconds.")

    start = time.time()
    part2_result = part2(input_file)
    elapsed = round(time.time() - start, 3)
    print(f"Part 2 result: {part2_result}. Took: {elapsed} seconds.")
