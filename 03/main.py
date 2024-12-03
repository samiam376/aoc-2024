import re


def read_input(is_example: bool):
    name = "example-input.txt" if is_example else "input.txt"
    with open(f"03/{name}", "r") as file:
        content = file.read()
        return content


def parse(s: str):
    """
    parse
    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    to (2*4 + 5*5 + 11*8 + 8*5)
    """

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return re.findall(pattern, s)


def read_num(s: str):
    n = ""
    idx = 0
    while idx < len(s) and s[idx].isdigit():
        n += s[idx]
        idx += 1

    return (n, idx)


def tokenize(s: str) -> list[str]:
    """
    xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
    """
    do = "do()"
    dont = "don't()"
    mul = "mul"
    tokens = []
    idx = 0
    while idx < len(s):
        if s.startswith(dont, idx):
            tokens.append(dont)
            idx += len(dont)
        elif s.startswith(do, idx):
            tokens.append(do)
            idx += len(do)
        elif s.startswith(mul, idx):
            next_idx = idx + 3
            if s[next_idx] != "(":
                idx += 1
                continue

            next_idx += 1
            (n1, n_idx_1) = read_num(s[next_idx:])
            if n1 == "":
                idx += 1
                continue

            next_idx += n_idx_1
            if s[next_idx] != ",":
                idx += 1
                continue

            next_idx += 1
            (n2, n_idx_2) = read_num(s[next_idx:])
            if n2 == "":
                idx += 1
                continue

            next_idx += n_idx_2
            if s[next_idx] != ")":
                idx += 1
                continue
            token = f"mul({n1},{n2})"
            tokens.append(token)
            idx += len(token)
        else:
            idx += 1
    return tokens


def pt1():
    m = read_input(False)
    p = parse(m)
    total = sum([int(x) * int(y) for x, y in p])
    print(total)


def pt2():
    m = read_input(False)
    tokens = tokenize(m)

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    s = 0
    do = True
    for t in tokens:
        if t == "do()":
            do = True
        elif t == "don't()":
            do = False
        else:
            match = re.match(pattern, t)
            if match and do:
                one = match.group(1)
                two = match.group(2)
                s += int(one) * int(two)
    print(s)


if __name__ == "__main__":
    pt2()
