from collections import Counter

with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_lines_temp = input_file.readlines()
    input_lines = [x.strip().split("-") for x in input_lines_temp]


def find_possible_destinations(position, this_route):
    paths = [x for x in input_lines if position in x]

    possible_destinations = []
    if paths:
        for path in paths:
            dest = next((x for x in path if x != position))
            if not (dest.islower() and dest in this_route) and dest != 'start':
                possible_destinations.append(dest)

        return possible_destinations
    else:
        return None


def find_possible_destinations_part_two(position, this_route):
    paths = [x for x in input_lines if position in x]
    small_cave_visits = Counter([x for x in this_route if x.islower()])

    possible_destinations = []
    if paths:
        for path in paths:
            dest = next((x for x in path if x != position))
            if dest != 'start':
                if any(x > 1 for x in list(small_cave_visits.values())):
                    if not (dest.islower() and dest in this_route):
                        possible_destinations.append(dest)
                else:
                    possible_destinations.append(dest)

        return possible_destinations
    else:
        return None


current_pos = 'start'

routes = 0
paths_to_check = [[current_pos, x] for x in find_possible_destinations(current_pos, [current_pos])]
while len(paths_to_check) != 0:
    route_check = paths_to_check[0]
    current_location = route_check[-1]

    destinations = find_possible_destinations_part_two(current_location, route_check)
    paths_to_check.remove(route_check)
    if destinations:
        for destination in destinations:
            current_route = route_check.copy()
            if destination == 'end':
                routes += 1
            else:
                current_route.append(destination)
                paths_to_check.append(current_route)

print(routes)
