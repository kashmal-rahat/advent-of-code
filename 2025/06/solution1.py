with open('input1.txt','r') as f:
    input_data = [line.strip() for line in f.readlines()]


matrix = [[x for x in i.split(' ') if x != ''] for i in input_data]
matrix[:-1] = [[int(x) for x in row] for row in matrix[:-1]]

#Cummulating Rows
for row_index in range(1,len(matrix[:-1])):
    for column_index in range(len(matrix[row_index])):
        if matrix[-1][column_index] == '+' : 
            matrix[row_index][column_index] += matrix[row_index-1][column_index]
        else:
            matrix[row_index][column_index] *= matrix[row_index-1][column_index]

#Showing Final Cummulated Row
print("Final Result: ",sum(matrix[-2]))