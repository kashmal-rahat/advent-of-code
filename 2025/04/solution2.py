def sum_adjacent(grid, i, j):
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    return sum(grid[i+di][j+dj] for di, dj in directions)

def print_matrix(grid):
    for row in grid:
        print(' '.join(str(cell) for cell in row))

with open('input1.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]

grid = [[0 if char == '.' else 1 for char in row] for row in input]
rows, columns = len(grid), len(grid[0])

#added 0 padding around the grid for simplicity
grid = [[0] * (columns + 2)] + [[0] + row + [0] for row in grid] + [[0] * (columns + 2)] 
rows, columns = len(grid), len(grid[0])

total_count = 0
while True:
    counter = 0
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            if grid[i][j] == 1 and sum_adjacent(grid,i,j) < 4:
                grid[i][j] = 0 
                counter+=1
    # print_matrix(grid)
    # print(counter)
    total_count += counter
    if counter == 0: break

print(total_count)