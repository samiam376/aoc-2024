import os


def read_input():
    with open("01/input.txt", "r") as file:
        content = file.read()
        return content


def split(s: str):
    l, r = s.split("  ")
    return (l, r)


def pt1():
    f = read_input()
    left, right = zip(*[split(s) for s in f.split(("\n")) if s != ""])
    dist = [abs(int(x) - int(y)) for x, y in zip(sorted(left), sorted(right))]
    total = sum(dist)
    print(total)


if __name__ == "__main__":
    pt1()
