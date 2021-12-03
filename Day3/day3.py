with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_lines_temp = input_file.readlines()
    input_lines = [x.strip() for x in input_lines_temp]


def part_one():
    columns = len(input_lines[0])
    rows = len(input_lines)

    gamma_rate = ''
    for col in range(columns):
        col_sum = 0
        for line in input_lines:
            col_sum += int(line[col])

        if col_sum < rows/2:
            gamma_rate += '0'
        else:
            gamma_rate += '1'

    epsilon_rate = ''.join(['1' if x == '0' else '0' for x in gamma_rate])

    print(int(gamma_rate, 2)*int(epsilon_rate, 2))


def find_most_common(input_list, rating_type):
    transposed_input = list(map(list, zip(*input_list)))

    rows = len(input_list)
    most_common = []

    for col in transposed_input:
        col_sum = sum(map(int, col))
        if col_sum < rows/2:
            most_common.append('0')
        else:
            most_common.append('1')

    return most_common


def part_two():
    rating_results = {}

    for rating in ['oxy', 'co2']:
        current_list = input_lines
        current_pos = 0
        while True:
            most_common = find_most_common(current_list, rating_type=rating)

            next_list = []
            for line in current_list:
                if rating == 'oxy':
                    if line[current_pos] == most_common[current_pos]:
                        next_list.append(line)
                else:
                    if line[current_pos] != most_common[current_pos]:
                        next_list.append(line)

            if len(next_list) == 1:
                rating_results[rating] = next_list[0]
                break
            else:
                current_list = next_list
                current_pos += 1

    print(int(rating_results['oxy'], 2) * int(rating_results['co2'], 2))


part_two()