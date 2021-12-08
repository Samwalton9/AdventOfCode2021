with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_lines_temp = input_file.readlines()
    input_lines = [x.strip() for x in input_lines_temp]

input_values = [i.split(" | ")[0].split(" ") for i in input_lines]
output_values = [i.split(" | ")[1].split(" ") for i in input_lines]

unique_counts = [2, 3, 4, 7]

digit_letters = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9'
}


def part_one():
    count = 0
    for output in output_values:
        for value in output:
            if len(value) in unique_counts:
                count += 1

    print(count)


def part_two():
    output_sum = 0
    for digit_pos, input in enumerate(input_values):
        letter_mapping = {}
        lengths = [len(i) for i in input]

        # If a letter is in 3-digit number but not 2-digit, it's a
        letter_mapping['a'] = list(set(input[lengths.index(3)]) - set(input[lengths.index(2)]))[0]

        # Look at 4-letter number, get b/d by ignoring c/f from 2-letter.
        four_letter = input[lengths.index(4)]
        two_letter = input[lengths.index(2)]
        b_d = list(set(four_letter) - set(two_letter))

        # Look at 6-letter numbers. Whichever has only one of b/d, that is b.
        six_letters = [i for i, letters in enumerate(input) if len(letters) == 6]
        for indices in six_letters:
            letters = input[indices]
            if not all(elem in letters for elem in b_d):
                missing_letter = next((x for x in b_d if x in letters), None)
                letter_mapping['b'] = missing_letter

        # Look at b_d, whichever isn't b is d
        letter_mapping['d'] = next((x for x in b_d if x != letter_mapping['b']), None)

        # Look at 5-letter numbers. Whichever has both b and d; remove a. Remaining is f_g.
        five_letters = [i for i, letters in enumerate(input) if len(letters) == 5]
        for indices in five_letters:
            letters = input[indices]
            if all(elem in letters for elem in b_d):
                f_g = [x for x in letters if x not in [letter_mapping['a'], letter_mapping['b'], letter_mapping['d']]]

        # Whichever of f_g is in the 2-letter number is f
        letter_mapping['f'] = next((x for x in f_g if x in two_letter), None)

        # Remaining two-letter character is c
        c = [x for x in two_letter if x != letter_mapping['f']]
        letter_mapping['c'] = c[0]

        # Find 5-letter with only one of f_g
        for indices in five_letters:
            letters = input[indices]
            if not all(elem in letters for elem in f_g):
                letter_mapping['g'] = next((x for x in f_g if x in letters), None)

        # e is the remaining letter
        current_letters = [x for _, x in letter_mapping.items()]
        remaining_letter = [x for x in 'abcdefg' if x not in current_letters]
        letter_mapping['e'] = remaining_letter[0]

        # ---------------------------
        # Calculate output values

        output_digits = output_values[digit_pos]

        digits_string = ''
        for digit in output_digits:
            letters_unscrambled = ''
            for letter in digit:
                # Reverse lookup, finding keys from values
                mapped_letter = list(letter_mapping.keys())[list(letter_mapping.values()).index(letter)]
                letters_unscrambled += mapped_letter

            sorted_letters = "".join(sorted(letters_unscrambled))
            digits_string += digit_letters[sorted_letters]

        this_output = int(digits_string)
        output_sum += this_output

    print(output_sum)


part_two()
