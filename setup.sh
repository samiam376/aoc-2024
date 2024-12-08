#!/bin/bash

# Check if a number argument is provided
if [ -z "$1" ]; then
  echo "Please provide a problem number"
  echo "Usage: ./setup.sh <number>"
  exit 1
fi

# Create directory with the provided number
mkdir -p "$1"

# Create main.py with template code
cat >"$1/main.py" <<EOL
def read_input(is_example: bool):
    name = "example-input.txt" if is_example else "input.txt"
    with open(f"$1/{name}", "r") as file:
        content = file.read()
        return content

def pt1():
    pass


def pt2():
    pass

if __name__ == "__main__":
    pt1()
EOL

# Create example-input.txt (empty)
touch "$1/example-input.txt"

# Create input.txt (empty)
touch "$1/input.txt"

echo "Created folder '$1' with main.py, example-input.txt, and input.txt"
