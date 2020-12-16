import time
import numpy


def parse_to_dict(input_list):
    input_dict = {
        "your ticket": [],
        "nearby tickets": [],
        "fields": []
    }

    for line in input_list:
        current = line.split(":")
        if current[0] in input_dict.keys():
            if current[0] == "your ticket":
                values = current[1].replace("\n", "").split(",")
                for val in values:
                    input_dict[current[0]].append(int(val))
            else:
                # parse nearby tickets into one list
                values = current[1].split("\n")[1:-1]
                for val in values:
                    input_dict[current[0]].append(
                        [int(t) for t in val.split(',')])

        else:
            current = line.split("\n")
            for field in current:
                temp = field.split(":")
                input_dict[temp[0]] = []
                values = temp[1].split(" or ")
                for sub in values:
                    sub = sub.strip().split("-")
                    sub_range = [*range(int(sub[0]), int(sub[1])+1)]
                    input_dict["fields"] += sub_range
                    input_dict[temp[0]].append((int(sub[0]), int(sub[1])))

    return input_dict


def part1(input_dict):
    part1_result = []
    to_remove = []
    for nearby_ticket in input_dict["nearby tickets"]:
        flag = False
        for val in nearby_ticket:
            if val not in input_dict["fields"]:
                flag = True
                part1_result.append(val)
        if flag:
            to_remove.append(nearby_ticket)
    for ticket in to_remove:
        input_dict["nearby tickets"].remove(ticket)

    return sum(part1_result), input_dict


def part2(input_dict):
    input_dict["nearby tickets"] = numpy.array(input_dict["nearby tickets"])
    target_fields = [key for key in input_dict.keys() if key not in [
        "your ticket", "nearby tickets", "fields"]]
    result_dict = {}

    for field in target_fields:
        result_dict[field] = []
        for i in range(len(input_dict["your ticket"])):
            if all((input_dict[field][0][0] <= elem <= input_dict[field][0][1]) or (input_dict[field][1][0] <= elem <= input_dict[field][1][1]) for elem in input_dict["nearby tickets"][:, i]):
                result_dict[field].append(i)

    result = 1
    found_idx = []
    converged = False
    while not converged:
        for key, val in result_dict.items():
            if len(val) == 1:
                if val[0] not in found_idx:
                    found_idx.append(val[0])
                    if "departure" in key:
                        result *= input_dict["your ticket"][val[0]]
            else:
                for col in val:
                    if col in found_idx:
                        val.remove(col)
        if len(found_idx) == len(result_dict):
            converged = True

    return result


if __name__ == "__main__":
    with open("../input/day16.txt") as f:
        input_list = f.read().split("\n\n")

    # Get into an organized format
    input_dict = parse_to_dict(input_list)

    start = time.time()
    part1_result, input_dict = part1(input_dict)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1 result: {part1_result}. Took {elapsed} seconds.")

    start = time.time()
    part2_result = part2(input_dict)
    elapsed = round(time.time() - start, 3)
    print(f"Part 2 result: {part2_result}. Took {elapsed} seconds.")
