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


print(trebuchet_with_letters())
