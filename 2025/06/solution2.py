with open('input1.txt','r') as f:
    input_data = [line.rstrip('\n') for line in f.readlines()]

calculation,total,operation = 0,0,input_data[-1][0]

for col_index in range(len(input_data[0])):
    
    digit = ''
    for row_index in range(len(input_data)):
        if input_data[row_index][col_index] != ' ':
            digit = digit + input_data[row_index][col_index]
    
    if digit.strip() == '': continue

    if not digit[-1].isnumeric(): #Identifying operator as a separator for each calculation
        total += calculation
        operation = digit[-1]
        calculation = 0 if operation == '+' else 1
        digit = digit[:-1]
    
    calculation = calculation + int(digit) if operation == '+' else calculation * int(digit)
    
total+=calculation
    

print("Final Result: ", total)
