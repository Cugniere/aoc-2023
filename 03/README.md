# Day 3: Gear Ratios

[Instructions](https://adventofcode.com/2023/day/3)

## Part One

There are many ways to solve that problem, the easiest way I thought of was to check each cell of the grid for numbers. Then when I got a 'complete' number, I check the surrounding part of the grid for symbol.

It would be possible to optimize this code in many ways but again I don't have a lot of time to spend on today's problem and I don't know if any of this code will be reusable for part two:
```python
def is_symbol(value):
    return value != "." and not value.isnumeric()


def valid_group(grid, x, y, length):
    w, h = len(grid[0]), len(grid)
    start_x, end_x = max(0, x - length - 1), min(x + 1, w)
    start_y, end_y = max(0, y - 1), min(y + 2, h)
    return any(
        [
            is_symbol(grid[y][x])
            for x in range(start_x, end_x)
            for y in range(start_y, end_y)
        ]
    )


def gear_ratio():
    with open("./input") as file:
        lines = [line.strip() for line in file][:-1]
    width, height = len(lines[0]), len(lines)
    total = 0
    for y in range(height):
        current_number = ""
        for x in range(width):
            if lines[y][x].isnumeric():
                current_number += lines[y][x]
            else:
                if len(current_number) and valid_group(
                    lines, x, y, len(current_number)
                ):
                    total += int(current_number)
                current_number = ""
        if len(current_number) and valid_group(lines, x, y, len(current_number)):
            total += int(current_number)
    return total

```

## Part Two

As expected almost none of the previous code is reusable as is. Here we are almost required to check each `*` for surrounding numbers so the easiest and dirtiest way would be to use a condition for all possibilities. I've tried do avoid that scenario by using regex and especially Python [finditer](https://docs.python.org/3/library/re.html#re.finditer)

```python
import re


def find_valid_numbers(line, x):
    numbers = []
    matches = re.finditer("(\d+)", "".join(line))
    for match in matches:
        if (match.start() >= x - 1 and match.start() <= x + 1) or (
            match.end() > x - 1 and match.end() <= x + 2
        ):
            numbers.append(match.group())
    return numbers


def compute_gear_ratio():
    with open("./input") as file:
        lines = [line.strip() for line in file][:-1]
    result = 0
    width, height = len(lines[0]), len(lines)
    for y in range(height):
        for x in range(width):
            if lines[y][x] == "*":
                adjacents = []
                if y > 0:
                    adjacents.extend(find_valid_numbers(lines[y - 1], x))
                adjacents.extend(find_valid_numbers(lines[y], x))
                if y < height - 1:
                    adjacents.extend(find_valid_numbers(lines[y + 1], x))
                if len(adjacents) == 2:
                    result += int(adjacents[0]) * int(adjacents[1])
    return result

```
