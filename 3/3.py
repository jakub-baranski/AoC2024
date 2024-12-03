import re

test_inp = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

test_inp_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def get_input():
    with open("input.txt") as f:
        return f.read()

MUL_REGEX = r"mul\((\d+),(\d+)\)"

def part_one():
    inp = get_input()
    matches = re.findall(MUL_REGEX, inp)
    print(sum([int(match[0]) * int(match[1]) for match in matches]))


def part_two():
    inp = get_input()
    do_indexes = [m.start() for m in re.finditer('do\(\)', inp)]
    dont_indexes = [m.start() for m in re.finditer("don't\(\)", inp)]

    state = {}

    current_state = 1
    for i in range(len(inp)):
        if i in do_indexes:
            state[i], current_state = 1, 1
        elif i in dont_indexes:
            state[i], current_state = 0, 0
        else:
            state[i] = current_state

    matches = re.finditer(MUL_REGEX, inp)

    print(sum([int(match.group(1)) * int(match.group(2)) for match in matches if state[match.start()] == 1]))


if __name__ == "__main__":
    part_one()
    part_two()
