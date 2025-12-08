import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def get_root(x):
    while parent[x] != x:
        x = parent[x]
    return x

with open('input1.txt', 'r') as f:
    coordinates = [tuple(map(int, line.strip().split(','))) for line in f]

num_connections=1000
n = len(coordinates)
parent = list(range(n))
size = [1] * n
pairs = []

for i in range(n):
    for j in range(i + 1, n):
        d = calculate_distance(coordinates[i], coordinates[j])
        pairs.append((d, i, j))
pairs.sort()

for idx, (d, i, j) in enumerate(pairs[:num_connections], 1):
    pi,pj = get_root(i),get_root(j)
    if pi!=pj:
        parent[pj] = parent[pi]
        size[pi]+=size[pj]

circuit_sizes = sorted([size[i] for i in range(n) if parent[i] == i], reverse=True)
print("Final Answer: ", circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2])


