import time


def get_last_number(puzzle_input, no_idx=2020):
    spoken = {number: [i+1] for i, number in enumerate(puzzle_input)}

    i = len(puzzle_input) + 1
    last_number = puzzle_input[-1]

    while True:
        if i == no_idx+1:
            break
        if len(spoken[last_number]) < 2:
            last_number = 0
        elif len(spoken[last_number]) >= 2:
            last_number = spoken[last_number][-1] - spoken[last_number][-2]

        if last_number in spoken.keys():
            spoken[last_number].append(i)
        else:
            spoken[last_number] = [i]

        i += 1

    return last_number


if __name__ == "__main__":
    puzzle_input = [0, 8, 15, 2, 12, 1, 4]

    start = time.time()
    part1_result = get_last_number(puzzle_input, no_idx=2020)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1 answer: {part1_result}. Took: {elapsed} seconds.")

    start = time.time()
    part2_result = get_last_number(puzzle_input, no_idx=30000000)
    elapsed = round(time.time() - start, 3)
    print(f"Part 2 answer: {part2_result}. Took: {elapsed} seconds.")
