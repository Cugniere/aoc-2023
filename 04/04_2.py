import re


def count_cards(card_map, index, count):
    count += 1
    for i in range(1, card_map[index] + 1):
        count = count_cards(card_map, index + i, count)
    return count


def scratchcards_rules():
    with open("./input") as file:
        count = 0
        card_map = {}
        for line in file:
            numbers = re.findall("(\d+)", line)
            if len(numbers):
                card_map[int(numbers[0])] = len(numbers[1:]) - len(set(numbers[1:]))
    for index in card_map:
        count = count_cards(card_map, index, count)

    return count


print(scratchcards_rules())
