def read_input(folder: str, is_example: bool):
    name = "example-input.txt" if is_example else "input.txt"
    with open(f"{folder}/{name}", "r") as file:
        content = file.read()
        return content
