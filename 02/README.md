# Day 2: Cube Conundrum

[Instructions](https://adventofcode.com/2023/day/2)

## Part One

The first part of the second day is pretty easy; we just need to read each line properly and check that each count of cube of a specific color is inferior or equal to the maximum amount.
```python
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

```
I used a regex to match all words and numbers in each line as well as the pretty useful `for ... else` syntax.

## Part Two

Not much to say about this second part, I don't really see a lot of place of improvements in term of complexity without making the code hard to read:

```python
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

```
