import math
from collections import Counter

with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_lines_temp = input_file.readlines()
    input_lines = [x.strip() for x in input_lines_temp]

rules = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in input_lines[2:]}


def part_one():
    template = input_lines[0]

    for _ in range(10):
        new_template = ''

        for i in range(len(template)-1):
            pair = template[i] + template[i+1]
            new_template += template[i] + rules[pair]
            if i == len(template)-2:
                new_template += template[i+1]

        template = new_template

        count_elements = Counter(template)

    print(count_elements.most_common()[0][1] - count_elements.most_common()[-1][1])


def part_two():
    template = input_lines[0]
    character_pairs = {}

    for i in range(len(template) - 1):
        pair = template[i] + template[i + 1]
        if pair in character_pairs:
            character_pairs[pair] += 1
        else:
            character_pairs[pair] = 1

    for _ in range(40):
        new_character_pairs = {}

        for pair, count in character_pairs.items():
            for new_pair_key in [pair[0] + rules[pair], rules[pair] + pair[1]]:
                if new_pair_key in new_character_pairs:
                    new_character_pairs[new_pair_key] += count
                else:
                    new_character_pairs[new_pair_key] = count

        character_pairs = new_character_pairs

    # This counting is wrong, double counting from the pairs.
    # Real values are half except for odd values which are half+0.5
    character_dict = {}
    for pair, count in character_pairs.items():
        for character in pair:
            if character in character_dict:
                character_dict[character] += count
            else:
                character_dict[character] = count

    dict_values = character_dict.values()
    print(math.ceil(max(dict_values)/2) - math.ceil(min(dict_values)/2))  # Double counting, except for odd numbers (start and end) which should round up.


part_one()
part_two()
