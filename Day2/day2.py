input = open('input.txt', 'r', encoding='utf-8')

input_lines_temp = input.readlines()
input_lines = [x.strip() for x in input_lines_temp]

def part_one():
    horizontal = 0
    vertical = 0
    for line in input_lines:
        split_line = line.split(" ")
        direction = split_line[0]
        distance = int(split_line[1])
        if direction == "forward":
            horizontal += distance
        elif direction == "down":
            vertical += distance
        elif direction == "up":
            vertical -= distance

    print(vertical*horizontal)

def part_two():
    aim = 0
    horizontal = 0
    vertical = 0
    for line in input_lines:
        split_line = line.split(" ")
        direction = split_line[0]
        distance = int(split_line[1])

        if direction == "up":
            aim -= distance
        elif direction == "down":
            aim += distance
        elif direction == "forward":
            horizontal += distance
            vertical += aim*distance

    print(horizontal*vertical)

part_two()