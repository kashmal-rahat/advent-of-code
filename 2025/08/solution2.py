import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def get_root(x):
    while parent[x] != x:
        x = parent[x]
    return x

with open('input1.txt', 'r') as f:
    coordinates = [tuple(map(int, line.strip().split(','))) for line in f]

n = len(coordinates)
parent = list(range(n))
size = [1] * n
pairs = []
last_pair = (0,0)

for i in range(n):
    for j in range(i + 1, n):
        d = calculate_distance(coordinates[i], coordinates[j])
        pairs.append((d, i, j))
pairs.sort()
for idx, (d, i, j) in enumerate(pairs, 1):
    pi,pj = get_root(i),get_root(j)
    if pi!=pj:
        last_pair = (i,j)
        parent[pj] = parent[pi]
        size[pi]+=size[pj]
        

print("Last Pair: ",coordinates[last_pair[0]],coordinates[last_pair[1]])
print("Final Answer: ",coordinates[last_pair[0]][0]*coordinates[last_pair[1]][0])
       
