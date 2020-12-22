import time
import re
import numpy as np
from collections import defaultdict

TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3


class Image():
    def __init__(self, img_id, data):
        self.id = img_id
        self.data = data

    @staticmethod
    def from_input(lines):
        try:
            return Image(
                int(re.split(r'[ :]', lines[0])[1]),
                np.array([list(l) for l in lines[1:]]))
        except:
            import ipdb
            ipdb.set_trace()

    @staticmethod
    def from_data(data):
        return Image(None, data)

    @staticmethod
    def from_grid(grid, margin=0):
        data = np.concatenate([
            np.concatenate([img.data[margin:-margin, margin:-margin]
                            for img in row], axis=1)
            for row in grid], axis=0)
        return Image.from_data(data)

    @property
    def borders(self):
        # top, right, bottom, left
        return [
            ''.join(self.data[0, :]),
            ''.join(self.data[:, -1]),
            ''.join(self.data[-1, :]),
            ''.join(self.data[:, 0])]

    def variations(self):
        data = self.data.copy()
        for _ in range(4):
            data = np.rot90(data)
            yield Image(self.id, data)
        data = np.flip(data, axis=0)
        for _ in range(4):
            data = np.rot90(data)
            yield Image(self.id, data)

    def algin_borders(self, border, target_position):
        for img in self.variations():
            if img.borders[target_position] == border:
                return img

    def find(self, symbol):
        return np.c_[np.where(self.data == symbol)]

    def count(self, symbol):
        return len(self.find(symbol))

    def __getitem__(self, idxs):
        return self.data[idxs]


def get_adjacent_positions(x, y, img):
    return zip([(x, y+1), (x+1, y), (x, y-1), (x-1, y)], zip(img.borders, [BOTTOM, LEFT, TOP, RIGHT]))


def build_lookup_by_border(images):
    lookup = defaultdict(list)
    for img in images:
        for border in img.borders:
            lookup[border].append(img)
    return lookup


def to_matrix(img_lookup):
    (min_x, min_y), (max_x, max_y) = min(img_lookup), max(img_lookup)
    matrix = []

    for y in range(max_y, min_y-1, -1):
        new_row = []
        for x in range(min_x, max_x + 1):
            new_row.append(img_lookup[(x, y)])
        matrix.append(new_row)

    return matrix


def build_grid(start_img, images):
    available_images = build_lookup_by_border(images)

    x, y = 0, 0
    processed = {start_img.id}
    grid = {(x, y): start_img}

    open_positions = [*get_adjacent_positions(x, y, start_img)]

    while open_positions:
        (x, y), (border, border_position) = open_positions.pop()

        neighbors = [img for img in available_images.get(
            border, []) if img.id not in processed]

        if not neighbors:
            neighbors = [img for img in available_images.get(
                border[::-1], []) if img.id not in processed]

        if not neighbors:
            continue

        neighbor = neighbors[0]
        neighbor = neighbor.algin_borders(border, border_position)
        processed.add(neighbor.id)
        grid[(x, y)] = neighbor
        open_positions.extend(get_adjacent_positions(x, y, neighbor))

    return to_matrix(grid)


def find_monsters(image, monster):
    def monster_found_at(x, y):
        matches = [image[i, j] == '#' for i, j in monster.find('#') + (x, y)]
        return sum(matches) == monster.count('#')

    monster_found = False

    for x in range(image.data.shape[0] - monster.data.shape[0]):
        for y in range(image.data.shape[1] - monster.data.shape[1]):
            if monster_found_at(x, y):
                monster_found = True

                for i, j in monster.find('#') + (x, y):
                    image.data[i, j] = 'O'

    return monster_found


def count_characters_without_monster(image, monster):
    for img in image.variations():
        if find_monsters(img, monster):
            return img.count('#')


if __name__ == '__main__':
    with open('../input/day20.txt') as f:
        images = [Image.from_input(lines.splitlines())
                  for lines in f.read().split('\n\n') if lines.splitlines() != []]

    with open('../input/monster.txt') as f:
        monster = Image.from_data(
            np.array([list(l) for l in f.read().splitlines()]))

    start = time.time()
    grid = build_grid(images[0], images)
    part1 = grid[0][0].id * grid[0][-1].id * \
        grid[-1][0].id * grid[-1][-1].id
    elapsed = round(time.time() - start, 3)
    print(f"Part 1: {part1}. Took: {elapsed} seconds.")

    start = time.time()
    final = Image.from_grid(grid, margin=1)
    part2 = count_characters_without_monster(final, monster)
    elapsed = round(time.time() - start, 3)
    print(f"Part 2: {part2}. Took: {elapsed} seconds.")
