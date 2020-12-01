from numpy import loadtxt
import itertools
import time


def part1(expenses: list, target_sum=2020):
    for i, j in itertools.combinations(map(int, expenses), 2):
        if i + j == target_sum:
            return i*j


def part2(expenses: list, target_sum=2020):
    for i, j, k in itertools.combinations(map(int, expenses), 3):
        if i + j + k == target_sum:
            return i * j * k


if __name__ == "__main__":
    lines = loadtxt("../input/day1.txt", delimiter="\n", unpack=False)
    start = time.time()
    result = part1(lines)
    end = time.time()
    print(result)
    print(f"Level 1 took {round(end-start, 4)} seconds")

    start = time.time()
    result = part2(lines)
    end = time.time()
    print(result)
    print(f"Level 2 took {round(end-start, 4)} seconds")
