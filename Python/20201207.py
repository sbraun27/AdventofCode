import time


class Bag():
    def __init__(self, descriptor, color):
        self.parents = []
        self.children = {}

        self.desc = descriptor
        self.color = color
        self.name = f"{descriptor} {color}"

    def add_parent(self, parent, bags_required):
        parent.children[self] = bags_required
        self.parents.append(parent)

    def add_children(self, child, bags_required):
        child.add_parent(child, bags_required)
        self.children[child] = bags_required

    def add_all_parents(self, list_input):
        for line in list_input:
            words = line.split()
            if self.name in line:
                # Check if this is the parent or not
                if words[0] == self.desc and words[1] == self.color:
                    if "no other bags" in line:
                        self.children = None
                    continue
                else:
                    my_bag_index = [i for i in range(
                        len(words)-1) if words[i] == self.desc and words[i+1] == self.color][0]
                    parent = Bag(words[0], words[1])
                    self.add_parent(parent, words[my_bag_index-1])
                    parent.add_all_parents(list_input)

    def add_all_children(self, list_input):
        for line in list_input:
            words = line.split()
            if words[0] == self.desc and words[1] == self.color:
                if "no other bags" in line:
                    continue
                else:
                    temp = 4
                    for i in range(4, len(words[4:])+1, 4):
                        child = Bag(words[i+1], words[i+2])
                        self.add_children(child, int(words[i]))
                        temp = i
                        child.add_all_children(list_input)
                        del(i)
                        i = temp

    def traverse_parents(self, count=set()):
        for parent_node in self.parents:
            count.add(parent_node.name)
            count = parent_node.traverse_parents(count)

        return count

    def part2(self, rules):
        bags = 0
        bag_to_find = self.name

        bags_to_add = rules[bag_to_find]
        for search_item in bags_to_add:
            for _ in range(search_item[0]):
                bags_to_add.extend(rules[search_item[1]])

        for contents in bags_to_add:
            bags += contents[0]

        return bags


def parse_lines(lines):
    rules = {}
    for line in lines:
        rule_parts = line.split(" contain ")

        bag = rule_parts[0][:-5]

        bag_contents = []
        for content_part in rule_parts[1].split(", "):
            if content_part == "no other bags.":
                break

            if content_part[-1] == ".":
                content_part = content_part[:-5].strip()
            else:
                content_part = content_part[:-4].strip()

            content_count = int(content_part[0:1])
            content_color = content_part[2:]

            bag_contents.append((content_count, content_color))

        rules[bag] = bag_contents

    return rules


if __name__ == "__main__":
    with open("../input/day7.txt", "r") as f:
        files = f.read().splitlines()

    my_bag = Bag("shiny", "gold")
    start = time.time()
    my_bag.add_all_parents(files)
    parent_count = len(my_bag.traverse_parents())
    elapsed = round(time.time() - start, 3)
    print(f"Part 1: {parent_count}. It took: {elapsed} seconds")

    rules = parse_lines(files)
    start = time.time()
    child_count = my_bag.part2(rules)
    elapsed = round(time.time() - start, 3)
    print(f"Part 1: {child_count}. It took: {elapsed} seconds")
