test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

def return_false_on_index_error_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return False
    return wrapper


directions = [
    (0, 1),  # Right
    (0, -1),  # Left
    (1, 0),  # Down
    (-1, 0),  # Up
    (1, 1),  # Diagonal right-down
    (1, -1),  # Diagonal left-down
    (-1, 1),  # Diagonal right-up
    (-1, -1),  # Diagonal left-up
]

def search(grid, x, y, dx, dy):
    # prevent negative indexes when multiplied by dx, dy and 4

    try:
        word = ""
        for i in range(4):
            xi = x + i * dx
            yi = y + i * dy
            if xi < 0 or yi < 0:
                return False

            word += grid[xi][yi]
        if word == "XMAS":
            return True
    except IndexError:
        return False


def get_input():
    with open("input.txt") as f:
        return f.read()





def part_one():
    grid = [list(line) for line in get_input().split("\n")]

    count = 0
    for x in range(len(grid)):
        try:
            for y in range(len(grid[0])):
                if grid[x][y] == 'X':
                    for dx, dy in directions:
                        if search(grid, x, y, dx, dy):
                            print(dx, dy)
                            count += 1
        except IndexError:
            continue

    print(count)


# ----

@return_false_on_index_error_decorator
def check_forward_slash(grid, x, y):
    if x - 1 < 0 or y + 1 >= len(grid[0]):
        return False

    searched_letters = ["M", "S"]

    left_up = grid[x - 1][y - 1]
    right_down = grid[x + 1][y + 1]

    if left_up != right_down:
        return all([left_up in searched_letters, right_down in searched_letters])

    return False

@return_false_on_index_error_decorator
def check_back_slash(grid, x, y):
    if x + 1 >= len(grid) or y - 1 < 0:
        return False
    searched_letters = ["M", "S"]

    right_up = grid[x - 1][y + 1]
    left_down = grid[x + 1][y - 1]

    if right_up != left_down:
        return all([right_up in searched_letters, left_down in searched_letters])

    return False



def part_two():
    grid = [list(line) for line in get_input().split("\n")]

    count = 0

    for x in range(len(grid) - 0):
        for y in range(len(grid[0])):
            try:
                if grid[x][y] == "A":
                    if check_forward_slash(grid, x, y) and check_back_slash(grid, x, y):
                        count += 1
            except IndexError:
                continue

    print(count)



if __name__ == "__main__":
    part_one()
    # part_two()
