import numpy
import time


def extend_to_right(slope_map, steps):
    length = len(slope_map)

    for i, row in enumerate(slope_map):
        slope_map[i] = row * (length * steps[1] - 1)
    return slope_map


def find_path(slope_map, start_position=(0, 0), steps=(1, 3)):
    tree_count = 0

    rows = list(range(start_position[0], len(slope_map), steps[0]))
    columns = list(range(start_position[1], len(
        slope_map)*steps[1], steps[1]))

    for row, column in zip(rows, columns):
        if slope_map[row][column] == "#":
            tree_count += 1

    return tree_count


if __name__ == "__main__":
    slope_map = open("../input/day3.txt", "r")
    slope_map = slope_map.readlines()
    slope_map = [line.rstrip() for line in slope_map]
    slope_map = extend_to_right(slope_map, (1, 7))
    start = time.time()
    print(f"Part 1: {find_path(slope_map)}")
    end = time.time()
    print(f"Part 1 took: {end-start} seconds\n")

    part2_slopes = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))
    part2_counts = []
    start = time.time()
    for slope in part2_slopes:
        part2_counts.append(find_path(slope_map, steps=slope))
        print(f"\tFinished {slope}, count was: {part2_counts[-1]}")
    product = numpy.prod(part2_counts)
    print(f"Part 2: {product}")
    end = time.time()
    print(f"Part 2 took: {end - start} seconds")
