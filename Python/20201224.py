import re
from functools import reduce
from collections import defaultdict

BLACK, WHITE = 1, 0

DIRECTIONS = {
    'e': (1, 0),
    'w': (-1, 0),
    'se': (0.5, -1),
    'sw': (-0.5, -1),
    'ne': (0.5, 1),
    'nw': (-0.5, 1)}

NEIGHBORS = DIRECTIONS.values()


def add(coord1, coord2):
    return coord1[0] + coord2[0], coord1[1] + coord2[1]


def final_coord(steps):
    """return coord after following STEPS from origin"""
    return reduce(add, steps, (0, 0))


def get_initial_state(moves):
    """return initial BLACK/WHITE tiles"""
    tiles = defaultdict(int)
    for tile in [final_coord(steps) for steps in moves]:
        tiles[tile] = (tiles[tile] + 1) % 2
    return tiles


def num_black_neighbors(tile, tiles):
    """return colors of all six neighbors of TILE"""
    return sum([tiles[add(tile, step)] for step in NEIGHBORS])


def get_all_neighbor_coords(tiles):
    """return all coordinats adjacent to any existing tile"""
    return [add(tile, neighbor) for tile in tiles for neighbor in NEIGHBORS]


def update_tile(tile, color, tiles):
    """return new state BLACK/WHITE of given tile"""
    if color == BLACK:
        return num_black_neighbors(tile, tiles) in [1, 2]
    if color == WHITE:
        return num_black_neighbors(tile, tiles) == 2


def update_floor(tiles):
    """returns tiles after update step"""
    new_tiles = defaultdict(int)

    # add all neighbors, because they may have to flip
    new_tiles.update({
        **dict.fromkeys(get_all_neighbor_coords(tiles), 0),
        **tiles})

    # check update conditions
    for tile, color in new_tiles.items():
        new_tiles[tile] = update_tile(tile, color, tiles)

    return new_tiles


def evolve(tiles, epochs):
    """return state of floor after EPOCHS iterations"""
    for _ in range(epochs):
        tiles = update_floor(tiles)
    return tiles


with open('../input/day24.txt') as f:
    moves = [[DIRECTIONS[d] for d in re.findall('(se|sw|ne|nw|e|w)', line)]
             for line in f.read().splitlines()]

    tiles = get_initial_state(moves)
    print('part 1:', sum(tiles.values()))
    print('part 2:', sum(evolve(tiles, 100).values()))
