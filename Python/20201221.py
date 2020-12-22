import time
import operator
from itertools import permutations


def file_to_dict(file_input):
    ingredient_list = {}
    for ingredients, allergenes in file_input:
        for a in allergenes:
            if not ingredient_list.get(a):
                ingredient_list[a] = set(ingredients)
            ingredient_list[a] = ingredient_list[a] & set(ingredients)
    return ingredient_list


def find_allergens(file_input):
    ingredient_list = file_to_dict(file_input)
    return list(ingredient_list.values())[0].union(*list(ingredient_list.values())[1:])


def part1(file_input):
    dangerous_ingredients = find_allergens(file_input)
    return sum([ingredient not in dangerous_ingredients
                for ingredients, _ in file_input for ingredient in ingredients])


def find_allergen(file_input):
    ingredient_list = file_to_dict(file_input)
    ingredients = list(find_allergens(file_input))

    for assignment in permutations(ingredients, r=len(ingredients)):
        if all(ingredient in ingredient_list[allergen] for allergen, ingredient in zip(ingredient_list, assignment)):
            return zip(ingredient_list, assignment)


def part2(file_input):
    assignment = find_allergen(file_input)
    return ','.join([i for a, i in sorted(assignment, key=operator.itemgetter(0))])


if __name__ == '__main__':
    with open('../input/day21.txt') as f:
        file_input = [[portion.replace(',', '').split(' ')
                       for portion in line[:-2].split(' (contains ')] for line in f]

    start = time.time()
    part1_result = part1(file_input)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1: {part1_result}. Took: {elapsed} seconds.")

    start = time.time()
    part2_result = part2(file_input)
    elapsed = round(time.time() - start, 3)
    print(f"Part 2: {part2_result}. Took: {elapsed} seconds.")
