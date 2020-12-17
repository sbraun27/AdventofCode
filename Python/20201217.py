import time
import numpy


def is_valid_coord(coord, shape):
    return all(0 <= dim < shape[i] for i, dim in enumerate(coord))


def next_coord(coord, offset):
    return tuple(dim + offset for dim in coord)


def expand_dimensions(dims, extend=2):
    return tuple(numpy.array(dims) + [extend] * len(dims))


def loop_coordinates(shape, tolerance=0):
    if len(shape) == 1:
        for i in range(-tolerance, shape[0]+tolerance):
            yield (i,)
    else:
        for i in range(-tolerance, shape[0]+tolerance):
            for coord in loop_coordinates(shape[1:], tolerance):
                yield(i, *coord)


def find_adjacent(grid):
    for coord in loop_coordinates(grid.shape, tolerance=1):
        adjacent_idxs = tuple([slice(max(0, dim-1), dim+2) for dim in coord])
        if is_valid_coord(coord, grid.shape):
            store = grid[coord]
            grid[coord] = 0
            adjacent = grid[adjacent_idxs].copy()
            is_on = store
            grid[coord] = store
        else:
            adjacent = grid[adjacent_idxs].copy()
            is_on = 0
        yield coord, is_on, adjacent


def grow_space(grid, cycles=1):
    for cycle in range(cycles):
        updated_grid = numpy.zeros(expand_dimensions(grid.shape))
        for coord, is_on, adjacent in find_adjacent(grid):
            if is_on:
                updated_grid[next_coord(coord, 1)] = adjacent.sum() in [2, 3]
            else:
                updated_grid[next_coord(coord, 1)] = adjacent.sum() == 3
        grid = updated_grid
    return grid


if __name__ == '__main__':
    with open('../input/day17.txt') as f:
        input_file = f.read().splitlines()

    grid = numpy.array([[symbol == '#' for symbol in line]
                        for line in input_file])

    start = time.time()
    part1 = numpy.sum(grow_space(grid[None], cycles=6))
    elapsed = round(time.time() - start, 3)
    print(f"Part 1: {part1}. Took: {elapsed} seconds.")

    start = time.time()
    part2 = numpy.sum(grow_space(grid[None][None], cycles=6))
    elapsed = round(time.time() - start, 3)
    print(f"Part 1: {part2}. Took: {elapsed} seconds.")
