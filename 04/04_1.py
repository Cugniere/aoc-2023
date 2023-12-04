import re


def scratchcards():
    with open("./input") as file:
        total = 0
        for line in file:
            numbers = re.findall("(\d+)", line)[1:]
            if len(numbers) > len(set(numbers)):
                total += 2 ** (len(numbers) - len(set(numbers)) - 1)
    return total


print(scratchcards())
