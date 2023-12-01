# Day 1: Trebuchet?!

[Instructions](https://adventofcode.com/2023/day/1)

## Part One

This first part of today's challenge is a good warming up. The easiest way I can see is to use regex to remove all non numeric characters from the each line and take the first and last one of them.

It is important to note that on some lines there is only a single digit that need to be used as both start and end of the number.

My solution is pretty basic:
```python
import re


def trebuchet():
    total = 0
    with open("./input") as file:
        for line in file:
            value = re.sub(r"\D", "", line)
            if len(value):
                total += int(f"{value[0]}{value[-1]}")
    return total

```

## Part Two

For a first advent of code's day, this part two is surprisingly harder that I would have expected and it took me some attempts to find the correct answer. The trick here is to understand that a line with `heightwo` means that this word will be replaced by both `8` and `2`.

Instead of relying on regex I used a loop running on each index of the line and pushing number in a list:
```python
def trebuchet_with_letters():
    total = 0
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    with open("./input") as file:
        for line in file:
            value = []
            index = 0
            length = len(line)
            while index < length:
                if line[index].isnumeric():
                    value.append(line[index])
                else:
                    for i, number in enumerate(numbers):
                        if (
                            index + len(number) <= length
                            and number == line[index : index + len(number)]
                        ):
                            value.append(i + 1)
                index += 1
            if len(value):
                total += int(f"{value[0]}{value[-1]}")
    return total

```
This code is pretty inefficient since its complexity is `O^3` but I didn't had more time to spend on that problem that day.

