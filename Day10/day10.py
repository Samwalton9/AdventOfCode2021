with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_lines_temp = input_file.readlines()
    input_lines = [x.strip() for x in input_lines_temp]

chunk_map = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>',
}

error_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def part_one():
    illegal_sum = 0
    for line in input_lines:
        expected_closes = []
        for i, character in enumerate(line):
            if character in chunk_map:
                expected_closes.append(chunk_map[character])
            elif character == expected_closes[-1]:
                del expected_closes[-1]
            elif character != expected_closes[-1]:
                illegal_sum += error_points[character]
                break

    print(illegal_sum)


def part_two():

    completion_points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    total_scores = []
    for line in input_lines:
        total_score = 0
        expected_closes = []
        corrupted = False
        for i, character in enumerate(line):
            if character in chunk_map:
                expected_closes.append(chunk_map[character])
            elif character == expected_closes[-1]:
                del expected_closes[-1]
            elif character != expected_closes[-1]:
                corrupted = True
                break

        if not corrupted:
            completion_string = reversed(expected_closes)
            for string in completion_string:
                total_score *= 5
                total_score += completion_points[string]

            total_scores.append(total_score)

    sorted_scores = sorted(total_scores)
    print(sorted_scores[len(total_scores)//2])


part_two()
