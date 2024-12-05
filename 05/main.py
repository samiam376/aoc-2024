from typing import Mapping


def read_input(is_example: bool):
    name = "example-input.txt" if is_example else "input.txt"
    with open(f"05/{name}", "r") as file:
        content = file.read()
        return content


def mid(len: int):
    if len % 2 == 0:
        return len // 2
    return (len - 1) // 2


def pt1():
    content = read_input(False)
    rules = []
    updates = []
    for val in content.split("\n"):
        if "|" in val:
            rules.append(val.split("|"))
        elif "," in val:
            updates.append(val.split(","))

    """
    The first section specifies the page ordering rules, one per line.
    The first rule, 47|53, means that if an update includes both page number 47 and page number 53, then page number 47 must be printed at some point before page number 53. (47 doesn't necessarily need to be immediately before 53; other pages are allowed to be between them.)

    The second section specifies the page numbers of each update. Because most safety manuals are different, the pages needed in the updates are different too. The first update, 75,47,61,53,29, means that the update consists of page numbers 75, 47, 61, 53, and 29.

    To get the printers going as soon as possible, start by identifying which updates are already in the right order
    """

    rule_map: Mapping[str, list[str]] = {}
    for r in rules:
        fst, snd = r
        if fst in rule_map:
            rule_map[fst].append(snd)
        else:
            rule_map[fst] = [snd]

    # Idea: iterate over each update row and check that the rules are in the right order
    valid_updates = []
    for update in updates:
        valid = True
        seen = set()
        for u in update:
            # if we've seen the value that must come before it's invalid
            after = rule_map.get(u)
            if after and any(map(lambda a: a in seen, after)):
                valid = False
                break
            seen.add(u)
        if valid:
            valid_updates.append(update)

    # print(valid_updates)
    mids = [update[mid(len(update))] for update in valid_updates]
    print(sum(map(int, mids)))


def pt2():
    pass


if __name__ == "__main__":
    pt1()
