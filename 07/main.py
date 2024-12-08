from itertools import product


def read_input(is_example: bool):
    name = "example-input.txt" if is_example else "input.txt"
    with open(f"07/{name}", "r") as file:
        content = file.read()
        return content


def pt1():
    s = read_input(False).split("\n")[:-1]
    parsed = []
    for row in s:
        total, rest = row.split(":")
        nums = [int(n) for n in rest.split(" ") if n != ""]
        parsed.append((int(total), nums))

    final = 0
    for total, nums in parsed:
        is_true = False
        for ops in product(["+", "*"], repeat=len(nums) - 1):
            agg, *rest = nums
            assert len(rest) == len(ops)
            for n, op in zip(rest, ops):
                if op == "+":
                    agg += n
                else:
                    agg *= n
            if agg == total:
                is_true = True
                break
        if is_true:
            print(f"total: {total} is valid")
            final += total
        else:
            print(f"total: {total} is not valid")

    print(final)


def pt2():
    pass


if __name__ == "__main__":
    pt1()
