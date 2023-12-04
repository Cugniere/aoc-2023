# Day 4: Scratchcards

[Instructions](https://adventofcode.com/2023/day/4)

## Part One

This first part is pretty straightforward, I used a regex to extract all numbers on a line (minus the first one which is the card number) and then compare:
- the count of numbers per line
- the count of unique numbers per line using `set`

```python
import re


def scratchcards():
    with open("./input") as file:
        total = 0
        for line in file:
            numbers = re.findall("(\d+)", line)[1:]
            if len(numbers) > len(set(numbers)):
                total += 2 ** (len(numbers) - len(set(numbers)) - 1)
    return total

```

## Part Two

The second part is not much harder than the first one. I create a map between line number and number of won cards and then use a recursive function to count the result.

A pretty neet optimization would be to store the result of all subcards won on a card but I'm too lazy and don't have enough time to rewrite my code.

```python
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

```

Still, today's problem was probably the easiest since the start of this year advent of code.

