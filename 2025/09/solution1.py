
with open("input1.txt", "r") as f:
    input_data = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

max_product = 0
for i in range(len(input_data)):
    a1, b1 = input_data[i]
    for j in range(i + 1, len(input_data)):
        a2, b2 = input_data[j]
        product = (abs(a1 - a2) + 1) * (abs(b1 - b2) + 1)
        if product > max_product:
            max_product = product

print(max_product)



