import time


def check_message(message, rules):
    ultimate = [(message, rules[0])]

    while ultimate:
        msg, rule = ultimate.pop()

        if not msg and not rule:
            return True

        if not msg or not rule:
            continue

        if isinstance(rule[0], str) and rule[0] == msg[0]:
            ultimate.append((msg[1:], rule[1:]))

        if isinstance(rule[0], int):
            replace = rules[rule[0]]

            if isinstance(replace[0], list):
                for option in replace:
                    ultimate.append((msg, [*option, *rule[1:]]))
            elif isinstance(replace[0], str):
                ultimate.append((msg, [replace, *rule[1:]]))
            else:
                ultimate.append((msg, [*replace, *rule[1:]]))

    return False


def load_input(file):
    with open(file) as f:
        input_file = f.read().splitlines()

    rules = {}
    messages = []
    parsing_rules = True
    for line in input_file:
        if line == "":
            parsing_rules = False
            continue

        if parsing_rules:
            idx, rule = line.split(": ")

            if '"' in rule:
                rule = rule.replace('"', '')

            elif "|" in rule:
                rule = [[int(n) for n in pattern.split(" ")]
                        for pattern in rule.split(" | ")]

            else:
                rule = [int(n) for n in rule.split(" ")]

            rules[int(idx)] = rule

        else:
            messages.append(line)

    return rules, messages


if __name__ == "__main__":
    rules, messages = load_input("../input/day19.txt")

    start = time.time()
    part1 = [check_message(message, rules) for message in messages]
    part1 = sum(part1)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1: {part1}. Took: {elapsed} seconds.")

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    start = time.time()
    part2 = [check_message(message, rules) for message in messages]
    part2 = sum(part2)
    elapsed = round(time.time() - start, 3)
    print(f"Part 2: {part2}. Took: {elapsed} seconds.")
