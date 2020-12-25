import re
from functools import reduce
from collections import defaultdict
import time


black_indicator, white_indicator = 1, 0

direction_map = {
    "e": (1, 0),
    "w": (-1, 0),
    "se": (0.5, -1),
    "sw": (-0.5, -1),
    "ne": (0.5, 1),
    "nw": (-0.5, 1)}

neighbor_directions = direction_map.values()


def add(coord1, coord2):
    return coord1[0] + coord2[0], coord1[1] + coord2[1]


def final_coord(steps):
    return reduce(add, steps, (0, 0))


def get_initial_state(moves):
    tiles = defaultdict(int)
    for tile in [final_coord(steps) for steps in moves]:
        tiles[tile] = (tiles[tile] + 1) % 2
    return tiles


def num_black_neighbors(tile, tiles):
    return sum([tiles[add(tile, step)] for step in neighbor_directions])


def find_neighbors(tiles):
    return [add(tile, neighbor) for tile in tiles for neighbor in neighbor_directions]


def change_tile(tile, color, tiles):
    if color == black_indicator:
        return num_black_neighbors(tile, tiles) in [1, 2]
    if color == white_indicator:
        return num_black_neighbors(tile, tiles) == 2


def update_floor(tiles):
    new_tiles = defaultdict(int)

    new_tiles.update({
        **dict.fromkeys(find_neighbors(tiles), 0),
        **tiles})

    for tile, color in new_tiles.items():
        new_tiles[tile] = change_tile(tile, color, tiles)

    return new_tiles


def update_floor_days(tiles, days):
    for _ in range(days):
        tiles = update_floor(tiles)
    return tiles


with open("../input/day24.txt") as f:
    moves = [[direction_map[d] for d in re.findall("(se|sw|ne|nw|e|w)", line)]
             for line in f.read().splitlines()]

    tiles = get_initial_state(moves)
    start = time.time()
    part1 = sum(tiles.values())
    elapsed = round(time.time() - start, 3)
    print(f"Part 1: {part1}. Took: {elapsed} seconds.")

    start = time.time()
    part2 = sum(update_floor_days(tiles, 100).values())
    elapsed = round(time.time() - start, 3)
    print(f"Part 2: {part2}. Took: {elapsed} seconds.")
