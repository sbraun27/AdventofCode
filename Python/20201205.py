import time


def binary_partition(boarding_passes, max_row=127, max_column=7):
    results = []
    for boarding_pass in boarding_passes:
        rows = list(range(max_row+1))
        columns = list(range(max_column+1))
        for character in boarding_pass:
            if character in ["F", "B"]:
                if character == "F":
                    rows = rows[:len(rows)//2]
                else:
                    rows = rows[len(rows)//2:]
            elif character in ["L", "R"]:
                if character == "L":
                    columns = columns[:len(columns)//2]
                else:
                    columns = columns[len(columns)//2:]

        results.append(rows[0]*8+columns[0])

    return results


def find_missing_seat(seat_ids):
    for i, seat in enumerate(seat_ids[1:]):
        if seat - seat_ids[i] != 1:
            return seat - 1


if __name__ == "__main__":
    with open("../input/day5.txt", "r") as f:
        boarding_passes = f.read().splitlines()

    max_row = 127
    max_column = 7

    start = time.time()
    seat_ids = binary_partition(boarding_passes)
    max_id = max(seat_ids)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1 result: {max_id}. Took: {elapsed} seconds.")

    start = time.time()
    seat_ids.sort()
    your_seat = find_missing_seat(seat_ids)
    elapsed = round(time.time() - start, 3)
    print(f"Your seat is: {your_seat}. Part 2 took: {elapsed} seconds.")
