with open('input2.txt', 'r') as f:
    input_data = [line.strip() for line in f.readlines()]

ranges = [tuple(map(int,r.split('-'))) for r in input_data]
ranges.sort()

count = 0
merged_start,merged_end = -1, -1

for start,end in ranges:
    if end <= merged_end:
        continue
    if start <= merged_end:
        merged_start,merged_end = merged_end+1,end
    else:
        merged_start,merged_end = start,end
    count += (merged_end - merged_start) + 1

print(count)