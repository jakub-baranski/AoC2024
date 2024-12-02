from collections import Counter

test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""


def get_left_right(lines):

    left = []
    right = []

    for line in lines:
        try:
            left.append(int(line.split()[0]))
            right.append(int(line.split()[1]))
        except IndexError:
            continue

    return left, right


def part_one():
    inp = get_input_values()
    lines = inp.split("\n")

    left, right = get_left_right(lines)

    for line in lines:
        try:
            left.append(int(line.split()[0]))
            right.append(int(line.split()[1]))
        except IndexError:
            continue

    left_sorted = sorted(left)
    right_sorted = sorted(right)
    zipped = list(zip(left_sorted, right_sorted))
    distances = []

    for i in range(len(zipped)):
        distances.append(abs(zipped[i][0] - zipped[i][1]))

    print(sum(distances))


def part_two():
    inp = get_input_values()
    lines = inp.split("\n")

    left, right = get_left_right(lines)
    scores = []

    counted = Counter(right)

    for num in left:
        scores.append(num*counted[num])

    print(sum(scores))


def get_input_values() -> str:
    with open("input.txt") as file:
        return file.read()


if __name__ == "__main__":
    part_one()
    part_two()
