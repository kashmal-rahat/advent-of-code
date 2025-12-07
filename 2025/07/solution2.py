with open('input1.txt','r') as f:
    manifolds = [line.strip() for line in f.readlines()]


tachyon = manifolds[0].find('S')

memory = {}
def calculate(manifolds,tachyon):

    key = (len(manifolds), tachyon) #Memoization for optimization, otherwise recurrsion was taking ages
    if key in memory:
        return memory[key]
    
    if len(manifolds) == 1:
        return 2 if tachyon in {index for index,value in enumerate(manifolds[0]) if value == '^'} else 1
        
    if manifolds[0].find('^') == -1:
        memory[key] =  calculate(manifolds[1:],tachyon)
        return memory[key]
        
    if tachyon in {index for index,value in enumerate(manifolds[0]) if value == '^'}:
        memory[key] = calculate(manifolds[1:],tachyon-1) + calculate(manifolds[1:],tachyon+1)
        return memory[key]  
    
    memory[key] = calculate(manifolds[1:],tachyon)
    return memory[key]


print("Final Count:", calculate(manifolds[1:],tachyon))

    


