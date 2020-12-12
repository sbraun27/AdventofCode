import time


class ship():
    def __init__(self, actions, x=0, y=0):
        self.x = x
        self.y = y
        self.actions = actions
        self.facing = "E"

    def update_coordinates(self, x, y, direction, units):
        return {
            "N": (x, y+units),
            "S": (x, y-units),
            "E": (x+units, y),
            "W": (x-units, y)
        }[direction]

    def rotate_direction(self, direction, units):
        left_rotation = {
            "N": "W",
            "W": "S",
            "S": "E",
            "E": "N"
        }
        right_rotation = {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N"
        }

        rotations = units // 90
        if direction == "L":
            rotation_map = left_rotation
        else:
            rotation_map = right_rotation

        for _ in range(rotations):
            self.facing = rotation_map[self.facing]

    def part1(self):
        for direction, units in self.actions:
            if direction == "F":
                self.x, self.y = self.update_coordinates(
                    self.x, self.y, self.facing, units)
            elif direction in "NEWS":
                self.x, self.y = self.update_coordinates(
                    self.x, self.y, direction, units)
            else:
                self.rotate_direction(direction, units)
        return self.get_location()

    def rotate_waypoint(self, direction, units):
        rotations = units // 90
        if direction == "L":
            for _ in range(rotations):
                self.w_x, self.w_y = -self.w_y, self.w_x
        else:
            for _ in range(rotations):
                self.w_x, self.w_y = self.w_y, -self.w_x

    def part2(self, x=10, y=1):
        self.w_x = x
        self.w_y = y
        for direction, units in self.actions:
            if direction == "F":
                self.x, self.y = self.x + self.w_x * units, self.y + self.w_y * units
            elif direction in "NEWS":
                self.w_x, self.w_y = self.update_coordinates(
                    self.w_x, self.w_y, direction, units)
            else:
                self.rotate_waypoint(direction, units)
        return self.get_location()

    def get_location(self):
        return abs(self.x) + abs(self.y)


if __name__ == "__main__":
    with open("../input/day12.txt", "r") as f:
        input_file = f.read().splitlines()

    parsed_list = [(line[0], int(line[1:])) for line in input_file]

    start = time.time()
    ferry = ship(parsed_list)
    part1 = ferry.part1()
    elapsed = round(time.time() - start, 3)
    print(f"Part 1: {part1}. Took: {elapsed}")

    start = time.time()
    ferry = ship(parsed_list)
    part2 = ferry.part2()
    elapsed = round(time.time() - start, 3)
    print(f"Part 1: {part2}. Took: {elapsed}")
