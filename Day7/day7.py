import statistics

with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_lines_temp = input_file.readline()
    input_list_strings = input_lines_temp.strip().split(",")
    input_list = [int(x) for x in input_list_strings]


def part_one():
    median_pos = statistics.median(input_list)

    fuel_spend = sum([abs(x-median_pos) for x in input_list])
    print(fuel_spend)


def part_two():
    fuel_spend = []
    for i in range(max(input_list)):
        distances = [abs(pos-i) for pos in input_list]
        fuel_spend.append(sum([sum(range(1, distance+1)) for distance in distances]))

    print(min(fuel_spend))


part_two()
