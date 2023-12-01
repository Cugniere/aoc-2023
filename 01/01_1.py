import re


def trebuchet():
    total = 0
    with open("./input") as file:
        for line in file:
            value = re.sub(r"\D", "", line)
            if len(value):
                total += int(f"{value[0]}{value[-1]}")
    return total


print(trebuchet())
