
with open('input1.txt', 'r') as f:
    battery_banks = [line.strip() for line in f.readlines()]

def find_max(bank):
    max_val,max_index = 0,0
    for i in range(len(bank)): 
        if bank[i] > max_val:
            max_val = bank[i]
            max_index = i 
    return max_val,max_index+1

def compute_joltage(bank):
    si,ei = 0, len(bank) - 11
    index,joltage = 0,0
    for i in range(12):
        max_val,max_index = find_max(bank[si+index:ei+i])
        index += max_index
        joltage = joltage * 10 + max_val
    return joltage

total_joltage = 0
for bank in battery_banks:
    bank = [int(battery) for battery in bank]
    total_joltage += compute_joltage(bank)

print("Total Joltage:", total_joltage)