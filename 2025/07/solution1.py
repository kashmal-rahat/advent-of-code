with open('input1.txt','r') as f:
    manifolds = [line.strip() for line in f.readlines()]


tachyon = {manifolds[0].find('S')}
count = 0
for fold in manifolds[1:]:
    separators = {index for index,value in enumerate(fold) if value == '^'}
    if separators: 
        collisions = tachyon & separators
        for collision in collisions:
            tachyon.discard(collision)
            tachyon.add(collision-1)
            tachyon.add(collision+1)
            count+=1

print("Final Count: ",count)

    


