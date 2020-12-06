import time


def get_list_of_groups(all_group_answers: list):
    groups = []
    current_group = []
    for answer in all_group_answers:
        if answer == "":
            groups.append(current_group)
            current_group = []
            continue
        else:
            current_group.append(answer)

    groups.append(current_group)

    return groups


def find_num_answers(group_answers):
    cum_sum = 0
    for group in group_answers:
        current = "".join(group)
        cum_sum += len(set(current))

    return cum_sum


def find_all_answers(group_answers):
    cum_sum = 0

    for group in group_answers:
        if len(group) == 1:
            cum_sum += len(group[0])
        else:
            all_answers = set("".join(group))
            for answer in group:
                current_answers = [char for char in answer]
                all_answers = all_answers.intersection(current_answers)
            cum_sum += len(all_answers)

    return cum_sum


if __name__ == "__main__":
    with open("../input/day6.txt", "r") as f:
        answers = f.read().splitlines()

    answers = get_list_of_groups(answers)

    start = time.time()
    result = find_num_answers(answers)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1 answer: {result}. Part 1 took: {elapsed}")

    start = time.time()
    result2 = find_all_answers(answers)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1 answer: {result2}. Part 1 took: {elapsed}")
