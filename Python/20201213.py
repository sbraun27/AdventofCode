import time


def find_lowest_wait(leave_time, ID_list):
    min_wait = max(ID_list)
    bus_id = ID_list[0]
    for bus in ID_list:
        if (bus - (leave_time % bus) < min_wait):
            min_wait = bus-(leave_time % bus)
            bus_id = bus

    return min_wait * bus_id


def find_lowest_subsequent_times(ID_list):
    ts = 100000000000000
    lcm = 1
    for start, step in ID_list:
        while(ts + start) % step != 0:
            ts += lcm
        lcm *= step
    return ts


if __name__ == "__main__":
    with open("../input/day13.txt", "r") as f:
        input_list = f.read().splitlines()

    leaving_time = int(input_list[0])
    bus_IDs = input_list[1].split(",")
    bus_IDs = [int(idx) for idx in bus_IDs if idx.lower() != "x"]

    start = time.time()
    part1 = find_lowest_wait(leaving_time, bus_IDs)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1: {part1}. Took: {elapsed} seconds.")

    part2_list = [(i, int(bus))
                  for i, bus in enumerate(input_list[1].split(",")) if bus != "x"]

    start = time.time()
    lowest_time = find_lowest_subsequent_times(part2_list)
    elapsed = round(time.time() - start, 3)
    print(f"Part 2: {lowest_time}. Took: {elapsed} seconds.")
