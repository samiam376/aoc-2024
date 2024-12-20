def read_input(folder: str, is_example: bool):
    name = "example-input.txt" if is_example else "input.txt"
    with open(f"{folder}/{name}", "r") as file:
        content = file.read()
        return content


def is_safe(row: list[int]) -> bool:
    """
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
    """
    assert len(row) >= 2
    inc = None
    for cur_idx in range(len(row) - 1):
        cur = row[cur_idx]
        next = row[cur_idx + 1]
        diff = abs(cur - next)
        if diff == 0 or diff > 3:
            return False

        is_inc = next - cur > 0

        if inc is None:
            inc = is_inc
        elif inc != is_inc:
            return False

    return True


def is_safe_damp(row: list[int]) -> bool:
    """
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
    Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
    """
    safe = is_safe(row)
    if safe:
        return True
    else:
        for i in range(len(row)):
            safe = safe or is_safe([*row[:i], *row[i + 1 :]])
    return safe


def pt1():
    s = read_input("02", False)
    m = [list(map(int, r.split(" "))) for r in s.split("\n")[:-1]]
    c = list(filter(lambda x: x, map(is_safe, m)))
    print(len(c))


def pt2():
    s = read_input("02", False)
    m = [list(map(int, r.split(" "))) for r in s.split("\n")[:-1]]
    c = list(filter(lambda x: x, map(is_safe_damp, m)))
    print(len(c))


if __name__ == "__main__":
    pt2()
