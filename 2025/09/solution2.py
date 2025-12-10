def is_valid_coordinate(x, y):
    for i in range(n):
        x1,y1,x2,y2 = *floor[i], *floor[(i+1) % n]
        if x1 == x2 == x and min(y1,y2) <= y <= max(y1,y2): return True
        if y1 == y2 == x and min(x1,x2) <= y <= max(x1,x2): return True 
    count = 0
    for i in range(n):
        x1,y1,x2,y2 = *floor[i], *floor[(i+1) % n]
        if y1 == y2: continue
        if y1 > y2: x1,y1,x2,y2 = x2,y2,x1,y1
        if y1 <= y < y2 and x < x1 + (y-y1) * (x2-x1) / (y2-y1): count += 1
    return count % 2 == 1

def is_valid_rectangle(x1, y1, x2, y2):
    a,b,c,d = min(x1,x2), max(x1,x2), min(y1,y2), max(y1,y2)
    if not is_valid_coordinate(a, d) or not is_valid_coordinate(b, c): return False
    for y in ys:
        if c < y < d and (not is_valid_coordinate(a, y) or not is_valid_coordinate(b, y)): return False
    for x in xs:
        if a < x < b and (not is_valid_coordinate(x, c) or not is_valid_coordinate(x, d)): return False
    return True

with open("input1.txt") as f:
    floor = [tuple(map(int, l.split(','))) for l in f]

xs, ys = sorted(set(x for x,y in floor)), sorted(set(y for x,y in floor))
n,answer = len(floor),0


for i, (x1,y1) in enumerate(floor):
    for x2,y2 in floor[i+1:]:
        if is_valid_rectangle(x1,y1,x2,y2):
            answer = max(answer, (abs(x1-x2)+1) * (abs(y1-y2)+1))

print("Final answer: ", answer)
