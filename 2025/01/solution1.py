with open('input1.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

counter = 0
starting_point = 50

for line in data:
    direction, rotation = line[0], int(line[1:])
    starting_point = (starting_point + rotation if direction == 'R' else starting_point - rotation) % 100
    if starting_point == 0:
        counter += 1

print(counter)
    