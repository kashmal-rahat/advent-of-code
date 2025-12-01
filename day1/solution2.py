with open('input1.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

counter = 0
starting_point = 50

for line in data:
    direction, rotation = line[0], int(line[1:])
    if direction == 'R':
        new_pos = starting_point + rotation
        counter += new_pos // 100 - starting_point // 100
    else:
        new_pos = starting_point - rotation
        counter += (starting_point - 1) // 100 - (new_pos - 1) // 100
    starting_point = new_pos % 100

print(counter)
    