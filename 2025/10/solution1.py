from itertools import product

def solve(lights, buttons):
    n = len(lights)
    target = [c == '#' for c in lights]
    min_presses = float('inf')
    for combo in product([0, 1], repeat=len(buttons)):
        state = [False] * n
        for press, btn in zip(combo, buttons):
            if press:
                for i in btn:
                    if i < n:
                        state[i] = not state[i] 
        if state == target:
            min_presses = min(min_presses, sum(combo))
    
    return min_presses


def parse(line):
    parts = line.split()
    lights = parts[0].strip('[]')
    buttons = [tuple(map(int, p.strip('()').split(','))) for p in parts[1:-1]]
    return lights, buttons

with open('input1.txt') as f:
    print("Final Answer: ", sum(solve(*parse(line)) for line in f if line.strip()))
