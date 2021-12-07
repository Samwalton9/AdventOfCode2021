from collections import Counter

with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_lines_temp = input_file.readline()
    input_list_strings = input_lines_temp.strip().split(",")
    input_list = [int(x) for x in input_list_strings]

time_to_birth = 6  # It's 7 but 0 is day 1
time_delay = 2


def part_one():
    num_days = 80

    for day in range(num_days):
        new_fish = []
        for i, fish_days in enumerate(input_list):
            if fish_days == 0:
                input_list[i] = time_to_birth
                new_fish.append(time_to_birth + time_delay)
            else:
                input_list[i] -= 1

        input_list.extend(new_fish)

    print(len(input_list))


def part_two():
    num_days = 256

    fish_dict = Counter(input_list)

    for x in range(num_days):
        for i in range(time_to_birth + time_delay + 1):
            if i == 0:
                num_birthed = fish_dict[i]
            else:
                fish_dict[i-1] = fish_dict[i]
        fish_dict[time_to_birth + time_delay] = num_birthed
        fish_dict[time_to_birth] += num_birthed

    print(sum(fish_dict.values()))

part_two()