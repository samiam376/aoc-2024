import itertools


def read_input(is_example: bool):
    name = "example-input.txt" if is_example else "input.txt"
    with open(f"08/{name}", "r") as file:
        content = file.read()
        return content


def pt1():
    input = read_input(False)
    cleaned = input.split("\n")[:-1]

    grid = {}
    cord_sets = {}
    for r_idx, row in enumerate(cleaned):
        for c_idx, char in enumerate(row):
            grid[(r_idx, c_idx)] = char
            if char == ".":
                continue

            if char in cord_sets:
                cord_sets[char].append((r_idx, c_idx))
            else:
                cord_sets[char] = [(r_idx, c_idx)]

    anti_nodes = set()
    for char in cord_sets:
        cords = cord_sets[char]
        for (r1, c1), (r2, c2) in itertools.combinations(cords, 2):
            r_dist = r1 - r2
            c_dist = c1 - c2
            n1 = (r1 + r_dist, c1 + c_dist)
            n2 = (r2 - r_dist, c2 - c_dist)
            anti_nodes.add(n1)
            anti_nodes.add(n2)

    f = [n for n in anti_nodes if n in grid]
    print(len(f))
    pass


def pt2():
    pass


if __name__ == "__main__":
    pt1()
