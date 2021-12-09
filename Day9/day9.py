with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_lines_temp = input_file.readlines()
    input_lines = [list(map(int, list(x.strip()))) for x in input_lines_temp]


def adjacent_point_values(x, y, array):
    if y == 0:
        up = None
    else:
        up = array[y-1][x]

    if x == 0:
        left = None
    else:
        left = array[y][x-1]

    try:  # So we don't need to know how long the rows/columns are
        down = array[y+1][x]
    except IndexError:
        down = None
    try:
        right = array[y][x+1]
    except IndexError:
        right = None

    return [left, right, up, down]


def adjacent_point_positions(x, y, array):
    if y == 0:
        up = None
    else:
        up = [y-1, x]

    if x == 0:
        left = None
    else:
        left = [y, x-1]

    if y+1 < len(array):
        down = [y+1, x]
    else:
        down = None
    if x+1 < len(array[0]):
        right = [y, x+1]
    else:
        right = None

    return [left, right, up, down]


# Edited to include a return useful for part 2
def part_one():
    risk_level_sum = 0
    low_point_positions = []
    for x_pos in range(len(input_lines[0])):
        for y_pos in range(len(input_lines)):
            value = input_lines[y_pos][x_pos]
            adjacent = adjacent_point_values(x_pos, y_pos, input_lines)

            if all([value < j for j in adjacent if j is not None]):
                low_point_positions.append([y_pos, x_pos])
                risk_level_sum += value+1

    print(risk_level_sum)
    return low_point_positions


def part_two():
    low_points = part_one()
    basin_sizes = []

    for point, position in enumerate(low_points):
        to_check = [position]
        already_checked = []
        basin_size = 0

        while len(to_check) > 0:
            y_pos, x_pos = to_check[0]
            adjacent_points = adjacent_point_positions(x_pos, y_pos, input_lines)
            to_check.extend([[i[0], i[1]]
                             for i in adjacent_points
                             if i is not None
                             and input_lines[i[0]][i[1]] != 9
                             and [i[0], i[1]] not in already_checked
                             and [i[0], i[1]] not in to_check])
            basin_size += 1

            to_check.pop(0)
            already_checked.append([y_pos, x_pos])

        basin_sizes.append(basin_size)

    sorted_basin_sizes = sorted(basin_sizes)
    top_sizes = sorted_basin_sizes[-3:]
    print(top_sizes[0]*top_sizes[1]*top_sizes[2])


part_two()
