from collections import Counter

with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_lines_temp = input_file.readlines()
    input_lines = [x.strip() for x in input_lines_temp]


def part_one():
    coords_list = []
    for line in input_lines:
        line_split = line.split(" -> ")
        one_split = line_split[0].split(",")
        two_split = line_split[1].split(",")

        x_coords = [int(one_split[0]), int(two_split[0])]
        y_coords = [int(one_split[1]), int(two_split[1])]

        x1 = x_coords[0]
        x2 = x_coords[1]
        if x1 > x2:
            x_range = range(x1, x2-1, -1)
        else:
            x_range = range(x1, x2 + 1)

        y1 = y_coords[0]
        y2 = y_coords[1]
        if y1 > y2:
            y_range = range(y1, y2-1, -1)
        else:
            y_range = range(y1, y2 + 1)

        if x1 == x2 or y1 == y2:
            if y1 == y2:
                coords_list.extend([f'{x_coord},{y1}' for x_coord in x_range])
            else:
                coords_list.extend([f'{x1},{y_coord}' for y_coord in y_range])

    sum_interactions = 0
    coord_count = Counter(coords_list)
    for coord, intersection in coord_count.items():
        if intersection > 1:
            sum_interactions += 1

    print(sum_interactions)


def part_two():
    coords_list = []
    for line in input_lines:
        line_split = line.split(" -> ")
        one_split = line_split[0].split(",")
        two_split = line_split[1].split(",")

        x_coords = [int(one_split[0]), int(two_split[0])]
        y_coords = [int(one_split[1]), int(two_split[1])]

        x1 = x_coords[0]
        x2 = x_coords[1]
        if x1 > x2:
            x_range = range(x1, x2-1, -1)
        else:
            x_range = range(x1, x2 + 1)

        y1 = y_coords[0]
        y2 = y_coords[1]
        if y1 > y2:
            y_range = range(y1, y2-1, -1)
        else:
            y_range = range(y1, y2 + 1)

        if x1 == x2 or y1 == y2:
            if y1 == y2:
                coords_list.extend([f'{x_coord},{y1}' for x_coord in x_range])
            else:
                coords_list.extend([f'{x1},{y_coord}' for y_coord in y_range])
        else:
            y_coord = y_coords[0]
            for x_coord in x_range:
                coords_list.append(f'{x_coord},{y_coord}')
                if y_coords[0] > y_coords[1]:
                    y_coord -= 1
                if y_coords[0] < y_coords[1]:
                    y_coord += 1

    sum_interactions = 0
    coord_count = Counter(coords_list)
    for coord, intersection in coord_count.items():
        if intersection > 1:
            sum_interactions += 1

    print(sum_interactions)


part_two()
