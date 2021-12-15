import matplotlib.pyplot as plt

with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_lines_temp = input_file.readlines()
    input_lines = [x.strip() for x in input_lines_temp]
    coordinates = [list(map(int, x.split(","))) for x in input_lines if "fold" not in x and x != '']
    instructions_temp = [x.split(" ")[2] for x in input_lines if "fold" in x]
    instructions = [[x.split("=")[0], int(x.split("=")[1])] for x in instructions_temp]


coordinate_array = coordinates
for instruction in instructions:
    folded_array = []
    for coordinate in coordinate_array:
        col = coordinate[0]
        row = coordinate[1]

        fold_coord = instruction[1]
        new_coord = coordinate

        if instruction[0] == "x" and col > fold_coord:
            new_coord = [fold_coord - (col - fold_coord), row]
        elif instruction[0] == "y" and row > fold_coord:
            new_coord = [col, fold_coord - (row - fold_coord)]

        if new_coord not in folded_array:
            folded_array.append(new_coord)

    coordinate_array = folded_array

    print(instruction, len(coordinate_array))

x_array = [x[0] for x in coordinate_array]
y_array = [10-x[1] for x in coordinate_array]  # Flip upside down

plt.scatter(x_array, y_array)
plt.ylim([-10, 25])
plt.show()
