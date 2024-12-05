from collections import defaultdict

test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def get_file_input() -> str:
    with open("input.txt") as f:
        return f.read()


def get_input_values():
    # inp = test_input
    inp=get_file_input()
    rules, numbers = inp.split("\n\n")
    rules_map = defaultdict(set)
    for rule in rules.split("\n"):
        key, value = rule.split("|")
        rules_map[key].add(value)
    return rules_map, [n.split(',') for n in numbers.split("\n")]


def part_one():
    rules, number_lines = get_input_values()
    correct_lines = []
    for line in number_lines:
        for i in range(len(line)):
            number = line[i]
            set_of_numbers_should_be_before = rules[number]
            if set_of_numbers_should_be_before.intersection(set(line[:i])):
                break

        else:
            correct_lines.append(line)

    print(
        sum([int(line[len(line) // 2]) for line in correct_lines[:-1] if line])
    )


def part_two():
    rules, number_lines = get_input_values()
    incorrect_lines = []
    for line in number_lines:
        for i in range(len(line)):
            number = line[i]
            set_of_numbers_should_be_before = rules[number]
            if set_of_numbers_should_be_before.intersection(set(line[:i])):
                incorrect_lines.append(line)
                break


    for line in incorrect_lines:
        for i in range(len(line)):
            number = line[i]
            set_of_numbers_should_be_before = rules[number]
            for j in range(len(line[:i])):
                if line[j] in set_of_numbers_should_be_before:
                    line[i], line[j] = line[j], line[i]
                    continue


    print(
        sum([int(line[len(line) // 2]) for line in incorrect_lines if line])
    )


if __name__ == "__main__":
    part_one()
    part_two()
