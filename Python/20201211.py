import time
import copy


def is_between(number, bottom, top):
    return bottom <= number < top


def check_seat(input_list, row_idx, col_idx, global_state):
    index_combinations = [(r, c) for r in [-1, 0, 1] for c in [-1, 0, 1]]
    index_combinations.remove((0, 0))

    no_rows = len(input_list[0])
    no_cols = len(input_list)

    current_state = input_list[row_idx][col_idx]

    target_seats = [(row_idx+r, col_idx + c) for r, c in index_combinations if is_between(
        row_idx+r, 0, no_rows) and is_between(col_idx+c, 0, no_cols)]
    adjacent_seats = [input_list[r][c] for r, c in target_seats]
    if current_state == "#":
        if adjacent_seats.count("#") >= 4:
            return False, "L"
        else:
            return global_state, "#"

    elif current_state == "L":
        if adjacent_seats.count("#") == 0:
            return False, "#"
        else:
            return global_state, "L"

    else:
        # Target seat is a floor, do nothing
        return global_state, "."


def check_seat2(input_file, row_idx, col_idx, global_state):
    no_rows = len(input_file[0])
    no_cols = len(input_file)

    directions = [(vert, horiz) for vert in [-1, 0, 1] for horiz in [-1, 0, 1]]
    directions.remove((0, 0))

    current_state = input_file[row_idx][col_idx]

    seen_seats = []
    # Find the 'seen' seats
    for row_inc, col_inc in directions:
        i = 1
        flagged = False
        while not flagged:
            target_row = row_idx + row_inc * i
            target_column = col_idx + col_inc * i
            if (not is_between(target_row, 0, no_rows)) or (not is_between(target_column, 0, no_cols)):
                break  # We can't check this move on to the next direction

            if input_file[target_row][target_column] != ".":
                seen_seats.append(input_file[target_row][target_column])
                flagged = True
            else:
                # The current seat is a floor, add one and move to the next seat
                i += 1

    if current_state == "#":
        if seen_seats.count("#") >= 5:
            return False, "L"
        else:
            return global_state, "#"
    elif current_state == "L":
        if seen_seats.count("#") == 0:
            return False, "#"
        else:
            return global_state, "L"
    else:
        return global_state, "."


def check_seating(input_file, check_function):
    state_change = True
    while state_change:
        new_list = copy.deepcopy(input_file)
        for r, _ in enumerate(input_file):
            for c, _ in enumerate(input_file):
                state_change, seat_state = check_function(
                    input_file, r, c, state_change)

                new_list[r][c] = seat_state

        input_file = new_list
        if state_change is False:
            # There was a change and we have to go again
            state_change = True
        else:
            # There was no change and we can break out
            break

    occupied_count = 0
    for i in input_file:
        occupied_count += i.count("#")

    return occupied_count


if __name__ == "__main__":
    with open("../input/day11.txt", "r") as f:
        input_list = f.read().splitlines()

    for i, row in enumerate(input_list):
        input_list[i] = [_ for _ in row]

    start = time.time()
    part1_answer = check_seating(input_list, check_seat)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1 answer: {part1_answer}. Took: {elapsed} seconds")

    start = time.time()
    part2_answer = check_seating(input_list, check_seat2)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1 answer: {part2_answer}. Took: {elapsed} seconds")
