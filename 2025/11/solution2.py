def dfs(node, path, has_dac, has_fft):
    
    if node in path:
        return
    new_has_dac = has_dac or (node == "dac")
    new_has_fft = has_fft or (node == "fft")
    
    memo_key = (node,new_has_dac,new_has_fft)
    if memo_key in memo and node not in path:
        count_both[0] += memo[memo_key]
        return
    
    path.append(node)
    before_both = count_both[0]
    
    if node == 'out':
        if new_has_dac and new_has_fft:
            count_both[0] += 1
    else:
        for next in graph.get(node, []):
            dfs(next, path, new_has_dac, new_has_fft)

    memo[memo_key] = count_both[0] - before_both
    path.pop()

count_both = [0]

with open("input1.txt", "r") as f:
    graph = {key: value.strip().split() for key, sep, value in (line.partition(': ') for line in f)}

memo = {}
dfs("svr", [], False, False)
print("Final Answer: ", count_both[0])

