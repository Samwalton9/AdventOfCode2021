with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_lines_temp = input_file.readlines()
    input_lines = [list(map(int,x.strip())) for x in input_lines_temp]

columns = len(input_lines)
rows = len(input_lines[0])


def adjacent_point_positions(col, row, array):
    # Initialise
    left, right, up, down, upleft, upright, downleft, downright = [None for _ in range(8)]

    if row != 0:
        up = [row-1, col]
        if col != 0:
            upleft = [row-1, col-1]
        if col+1 < len(array[0]):
            upright = [row-1, col+1]

    if row + 1 < len(array):
        down = [row + 1, col]
        if col != 0:
            downleft = [row+1, col-1]
        if col + 1 < len(array[0]):
            downright = [row+1, col+1]

    if col != 0:
        left = [row, col-1]

    if col+1 < len(array[0]):
        right = [row, col+1]

    return [left, right, up, down, upleft, upright, downleft, downright]


def part_one():
    flash_count = 0
    for time_step in range(100):
        flashes = []
        flashed = []
        for col in range(columns):
            for row in range(rows):
                input_lines[col][row] += 1
                if input_lines[col][row] > 9:
                    flashes.append([col, row])

        while flashes:
            for i, flash in enumerate(flashes):
                valid_adjacent_points = adjacent_point_positions(flash[0], flash[1], input_lines)
                for pos in valid_adjacent_points:
                    if pos:
                        row, col = pos[0], pos[1]
                        input_lines[col][row] += 1
                        if input_lines[col][row] > 9 and [col, row] not in flashes and [col, row] not in flashed:
                            flashes.append([col, row])
                flashes.pop(i)
                flashed.append(flash)
                flash_count += 1

        # Reset flashed octopuses
        for col in range(columns):
            for row in range(rows):
                if input_lines[col][row] > 9:
                    input_lines[col][row] = 0

    print(flash_count)


def part_two():
    not_synced = True
    time_step = 1
    while not_synced:
        flashes = []
        flashed = []
        for col in range(columns):
            for row in range(rows):
                input_lines[col][row] += 1
                if input_lines[col][row] > 9:
                    flashes.append([col, row])

        while flashes:
            for i, flash in enumerate(flashes):
                valid_adjacent_points = adjacent_point_positions(flash[0], flash[1], input_lines)
                for pos in valid_adjacent_points:
                    if pos:
                        row, col = pos[0], pos[1]
                        input_lines[col][row] += 1
                        if input_lines[col][row] > 9 and [col, row] not in flashes and [col, row] not in flashed:
                            flashes.append([col, row])
                flashes.pop(i)
                flashed.append(flash)

        if len(flashed) == columns*rows:
            print(time_step)
            not_synced = False

        # Reset flashed octopuses
        for col in range(columns):
            for row in range(rows):
                if input_lines[col][row] > 9:
                    input_lines[col][row] = 0

        time_step += 1

part_two()
