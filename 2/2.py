test_inp = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def get_input_values():
    with open("input.txt") as f:
        return f.read()

def part_one():
    inp = get_input_values()

    lines = inp.split("\n")

    safe_lines = 0


    for l in lines:
        if not l:
            continue
        sequence = list(map( lambda x: int(x), l.split()))
        rev = sequence[::-1]
        if not (sorted(sequence) == sequence or sorted(rev) == rev):
            continue
        for i in range(len(sequence) - 1):
            if sequence[i] == sequence[i + 1]:
                break
            change = abs(int(sequence[i]) - int(sequence[i + 1]))
            if change < 1 or change > 3:
                break
        else:
            safe_lines += 1

    print(safe_lines)


def is_safe(line_str: str):
    sequence = list(map(lambda x: int(x), line_str.split()))
    rev = sequence[::-1]
    if not line_str:
        return False
    if not (sorted(sequence) == sequence or sorted(rev) == rev):
        return False
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            return False
        change = abs(int(sequence[i]) - int(sequence[i + 1]))
        if change < 1 or change > 3:
            return False
    return True


def part_two():
    inp = get_input_values()

    lines = inp.split("\n")

    safe_lines = 0

    unsafe_for_evaluation = []

    for l in lines:
        if is_safe(l):
            safe_lines += 1
        else:
            unsafe_for_evaluation.append(l)


    for l in unsafe_for_evaluation:
        for remove_index in range(len(l.split())):
            line = l.split()
            line.pop(remove_index)
            new_line = " ".join(line)
            if is_safe(new_line):
                safe_lines += 1
                break

    print(safe_lines)

if __name__ == "__main__":
    part_one()
    part_two()
