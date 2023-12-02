import re


def cube_power():
    set_power = 0
    with open("./input") as file:
        for line in file:
            groups = re.findall("(\d+|\w+)", line)
            if groups:
                colors = {"red": 0, "green": 0, "blue": 0}
                for index in range(2, len(groups), 2):
                    value, color = int(groups[index]), groups[index + 1]
                    if colors[color] < value:
                        colors[color] = value
                set_power += colors["red"] * colors["green"] * colors["blue"]
    return set_power


print(cube_power())
