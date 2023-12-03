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


print(compute_gear_ratio())
