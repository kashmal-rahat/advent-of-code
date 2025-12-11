def dfs(node, path):

    if node in path: return
    path.append(node)
    
    if node == 'out':
        paths.append(path)
    else:
        for next in graph.get(node):
            dfs(next,path)
    path.pop()

paths = []

with open("input1.txt","r") as f:
    graph = {key:value.strip().split() for key,sep,value in (line.partition(': ') for line in f.readlines())}

dfs("you",[])
print("Final Answer: ", len(paths))
    

    


