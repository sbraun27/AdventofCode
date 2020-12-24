import time


def numbers_to_dict(numbers):
    length = len(numbers)
    return {n: numbers[(i+1) % length] for i, n in enumerate(numbers)}


def move_cups(numbers, current, max_values):
    moved = (numbers[current], numbers[numbers[current]],
             numbers[numbers[numbers[current]]])

    destination = current - 1
    while destination in moved or destination == 0:
        destination = (destination - 1) % (max_values + 1)

    numbers[current] = numbers[moved[-1]]
    numbers[moved[-1]] = numbers[destination]
    numbers[destination] = moved[0]

    return numbers[current]


def crab_cups(numbers, rounds=10):
    numbers = numbers_to_dict(numbers)
    max_values = max(numbers.values())

    current = list(numbers.keys())[0]

    for _ in range(1, rounds+1):
        current = move_cups(numbers, current, max_values)

    results = []
    current = numbers[1]
    while len(results) < min(len(numbers)-1, 100):
        results.append(current)
        current = numbers[current]

    return results


if __name__ == '__main__':
    numbers = [3, 2, 7, 4, 6, 5, 1, 8, 9]
    start = time.time()
    part1 = crab_cups(numbers, 100)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1: {part1}. Took: {elapsed} seconds.")

    start = time.time()
    numbers = [3, 2, 7, 4, 6, 5, 1, 8, 9]
    numbers.extend(range(max(numbers)+1, 1000001))
    part2 = crab_cups(numbers, 10000000)
    elapsed = round(time.time() - start)
    print(f"Part 2: {part2[0] * part2[1]}. Took: {elapsed} seconds.")
