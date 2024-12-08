def read_input(is_example: bool):
    name = "example-input.txt" if is_example else "input.txt"
    with open(f"06/{name}", "r") as file:
        content = file.read()
        return content


directions = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
]


def rotate(cord):
    """
    (-1, 0) -> (0, 1)
    (0, 1) -> (1, 0)
    (1, 0) -> (0, -1)
    (0, -1) -> (-1, 0)
    """
    (row, col) = cord
    return (col, row * -1)


def add_tup(t1, t2):
    return tuple(x + y for x, y in zip(t1, t2))


def print_grid(grid, c_len, r_len):
    output = [[" " for _ in range(c_len)] for _ in range(r_len)]
    for (row, col), char in grid.items():
        output[row][col] = char
    print("\n".join("".join(row) for row in output))


def pt1():
    m = read_input(False)
    start = None
    grid = {}
    rows = m.split("\n")
    r_len = len(rows)
    c_len = len(rows[0])
    for r_idx, row in enumerate(rows):
        for c_idx, char in enumerate(row):
            cord = (r_idx, c_idx)
            if char == "^":
                start = cord
            grid[cord] = char

    """
    Idea: iterate over the grid and change directinos whenever an obstacle is encountared
    """
    # first dir is up
    dir = (-1, 0)
    current = start
    last = None
    while current in grid:
        char = grid[current]
        if char == "#":
            assert last is not None
            current = last
            dir = rotate(dir)
        else:
            grid[current] = "X"
            last = current
            current = add_tup(current, dir)
        # print_grid(grid, c_len, r_len)

    count = 0
    for char in grid.values():
        if char == "X":
            count += 1

    output = [[" " for _ in range(c_len)] for _ in range(r_len)]
    for (row, col), char in grid.items():
        output[row][col] = char
    print("\n".join("".join(row) for row in output))
    print(count)


def pt2():
    pass


if __name__ == "__main__":
    pt1()
