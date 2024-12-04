from typing import Set, Tuple


def read_input(is_example: bool):
    name = "example-input.txt" if is_example else "input.txt"
    with open(f"04/{name}", "r") as file:
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


def search(grid: list[list[str]], start: Tuple[int, int], direction: Tuple[int, int]):
    """search for xmas in a direction"""
    r_size, c_size = len(grid), len(grid[0])
    r, c = start
    rd, cd = direction

    seen = [(r, c)]
    xmas = "XMAS"
    idx = 0
    while True:
        if idx >= len(xmas):
            return seen

        if r < 0 or r >= r_size or c < 0 or c >= c_size:
            return None

        v = grid[r][c]
        if v != xmas[idx]:
            return None

        seen.append((r, c))
        idx += 1
        r = r + rd
        c = c + cd


def pt1():
    grid = list(map(list, read_input(False).split("\n")[:-1]))
    rows, cols = len(grid), len(grid[0])
    idxs = []
    count = 0
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            if v == "X":
                for dir in directions:
                    found = search(grid, (r, c), dir)
                    if found:
                        idxs += found
                        count += 1
    print(count)


def cords(r_size, c_size) -> Set[Tuple[int, int]]:
    s = set()
    for r in range(r_size):
        for c in range(c_size):
            s.add((r, c))
    return s


def search2(
    grid: list[list[str]],
    cord_set: Set[Tuple[int, int]],
    start: Tuple[int, int],
):
    """search for x-mas in a direction
    start with a -> m, s on diag
    """

    r, c = start

    can_see_left = ["M", "S"]
    can_see_right = ["M", "S"]

    # search all corners
    top_left = (r - 1, c - 1)
    if top_left not in cord_set:
        return 0

    tl_v = grid[top_left[0]][top_left[1]]
    if tl_v not in can_see_left:
        return 0

    can_see_left.remove(tl_v)

    top_right = (r - 1, c + 1)
    if top_right not in cord_set:
        return 0

    tr_v = grid[top_right[0]][top_right[1]]
    if tr_v not in can_see_right:
        return 0

    can_see_right.remove(tr_v)

    bottom_right = (r + 1, c + 1)
    if bottom_right not in cord_set:
        return 0

    br_v = grid[bottom_right[0]][bottom_right[1]]
    if br_v not in can_see_left:
        return 0

    bottom_left = (r + 1, c - 1)
    if bottom_left not in cord_set:
        return 0

    bl_v = grid[bottom_left[0]][bottom_left[1]]
    if bl_v not in can_see_right:
        return 0

    return 1


def pt2():
    grid = list(map(list, read_input(False).split("\n")[:-1]))
    rows, cols = len(grid), len(grid[0])
    cord_set = cords(rows, cols)
    count = 0
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            if v == "A":
                count += search2(grid, cord_set, (r, c))
    print(count)


if __name__ == "__main__":
    pt2()
