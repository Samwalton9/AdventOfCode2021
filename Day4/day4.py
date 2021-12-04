with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_lines = input_file.readlines()

bingo_numbers = input_lines[0].strip().split(",")

input_lines = input_lines[2:]


def get_boards(input_list):
    board_list = []
    for i in range(0, len(input_list), 6):
        board = input_list[i:i+5]

        # replace("  ", " ") because single-digit numbers have an extra space
        output_board = [line.strip().replace("  ", " ").split(" ") for line in board]

        board_list.append(output_board)

    return board_list


def part_one():
    bingo_boards = get_boards(input_lines)
    num_boards = len(bingo_boards)
    size = 5

    boolean_boards = [[[False, False, False, False, False] for _ in range(size)] for _ in range(num_boards)]

    victory = False

    for k, bingo_num in enumerate(bingo_numbers):
        for i, board in enumerate(bingo_boards):
            this_boolean_board = boolean_boards[i]
            for x in range(size):
                for y in range(size):
                    if board[x][y] == bingo_num:
                        this_boolean_board[x][y] = True

            # Check victory
            for row in this_boolean_board:
                if all(row):
                    victory = True

            for column in range(size):
                if all([this_boolean_board[x][column] for x in range(size)]):
                    victory = True

            if victory:
                unmarked_numbers = [board[a][b] for a in range(size) for b in range(size) if not this_boolean_board[a][b]]
                sum_unmarked = sum(map(int, unmarked_numbers))
                return print(sum_unmarked*int(bingo_num))


def part_two():
    bingo_boards = get_boards(input_lines)
    num_boards = len(bingo_boards)
    size = 5

    boolean_boards = [[[False, False, False, False, False] for _ in range(size)] for _ in range(num_boards)]
    finished_boards = [False for _ in range(num_boards)]

    for k, bingo_num in enumerate(bingo_numbers):
        for i, board in enumerate(bingo_boards):
            victory = False
            this_boolean_board = boolean_boards[i]
            for x in range(size):
                for y in range(size):
                    if board[x][y] == bingo_num:
                        this_boolean_board[x][y] = True

            # Check victory
            for row in this_boolean_board:
                if all(row):
                    victory = True

            for column in range(size):
                if all([this_boolean_board[x][column] for x in range(size)]):
                    victory = True

            if victory:
                finished_boards[i] = True
                if all(finished_boards):
                    unmarked_numbers = [board[a][b] for a in range(size) for b in range(size) if not this_boolean_board[a][b]]
                    sum_unmarked = sum(map(int, unmarked_numbers))
                    return print(sum_unmarked*int(bingo_num))


part_two()
