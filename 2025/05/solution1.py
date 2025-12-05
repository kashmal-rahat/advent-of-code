with open('input1.txt', 'r') as f:
    input_data = [line.strip() for line in f.readlines()]

split_index = input_data.index('')
ranges = [tuple(map(int, r.split('-'))) for r in input_data[:split_index]]
ids = [int(i) for i in input_data[split_index+1:]]

count = 0
for fresh_id in ids:
    for start,end in ranges:
        if  start <= fresh_id <= end:
            count+=1
            break

print(count)
