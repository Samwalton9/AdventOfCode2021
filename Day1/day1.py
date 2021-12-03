input = open('input.txt', 'r', encoding='utf-8')

input_lines_temp = input.readlines()
input_lines = [int(x.strip()) for x in input_lines_temp]


def part_1():
    increases = 0
    prior_depth = None
    for line in input_lines:
        depth = line
        if prior_depth:
            if depth > prior_depth:
                increases += 1

        prior_depth = depth

    print(increases)


def part_2():
    increases = 0
    prior_depth = None
    for i in range(len(input_lines)):
        depth_range = input_lines[i:i+3]
        if not len(depth_range) == 3:
            continue

        if prior_depth:
            if sum(depth_range) > sum(prior_depth):
                increases += 1

        prior_depth = depth_range

    print(increases)


part_2()
