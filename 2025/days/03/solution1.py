with open('input1.txt', 'r') as f:
    battery_banks = [line.strip() for line in f.readlines()]


def find_two_max(bank):
    max_val,max_index = 0,0
    for i in range(len(bank)-1):  #for readability, kept two loops separate
        if bank[i] > max_val:
            max_val = bank[i]
            max_index = i 
    second_max,second_index = 0,0

    for i in range(len(bank)):
        if bank[i] > second_max  and i > max_index:
            second_max = bank[i]
            second_index = i 

    return (second_max, max_val) if second_index < max_index else (max_val, second_max)    
        

total_joltage = 0
for bank in battery_banks:
    bank = [int(battery) for battery in bank]
    max_val,second_max = find_two_max(bank)
    total_joltage += (max_val*10) + second_max

print("Total Joltage:", total_joltage)

        
