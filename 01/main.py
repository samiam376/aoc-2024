import os


def read_input():
    with open("01/example-input.txt", "r") as file:
        content = file.read()
        return content


def pt1():
    f = read_input()
    left, right = zip(*[(s[0], s[-1]) for s in f.split(("\n")) if s != ""])
    dist = [abs(int(x) - int(y)) for x, y in zip(sorted(left), sorted(right))]
    total = sum(dist)
    print(total)


if __name__ == "__main__":
    pt1()
