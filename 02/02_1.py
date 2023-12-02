import re


def cube_conundrum():
    valid_game = 0
    limit = {"red": 12, "green": 13, "blue": 14}
    with open("./input") as file:
        for line in file:
            groups = re.findall("(\d+|\w+)", line)
            if groups:
                for index in range(2, len(groups), 2):
                    value, color = int(groups[index]), groups[index + 1]
                    if limit[color] < value:
                        break
                else:
                    valid_game += int(groups[1])
    return valid_game


print(cube_conundrum())
