import time
import operator


def find_operation(formula, part2):
    p_depth = 0
    arith_func = None
    for i, char in enumerate(reversed(formula)):
        if char == '(':
            p_depth += 1
        if char == ')':
            p_depth -= 1
        if char == '*' and p_depth == 0:
            arith_func = operator.mul, len(formula) - i - 1
            break
        if char == '+' and p_depth == 0:
            arith_func = operator.add, len(formula) - i - 1
            if not part2:
                break
    return arith_func


def evaluate_element(formula, part2=False):
    if formula.isdigit():
        return int(formula)

    operation = find_operation(formula, part2)

    if operation is None:
        return evaluate_element(formula[1:-1], part2)

    return operation[0](
        evaluate_element(formula[:operation[1]], part2),
        evaluate_element(formula[operation[1]+1:], part2))


if __name__ == '__main__':
    with open('../input/day18.txt') as f:
        input_file = f.read().splitlines()

    problems = [line.replace(' ', '') for line in input_file]

    start = time.time()
    part1_result = sum(evaluate_element(p) for p in problems)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1: {part1_result}. Took: {elapsed} seconds.")

    start = time.time()
    part2_result = sum(evaluate_element(p, part2=True) for p in problems)
    elapsed = round(time.time() - start, 3)
    print(f"Part 2: {part2_result}. Took: {elapsed} seconds.")
