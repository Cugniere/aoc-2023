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


print(gear_ratio())
