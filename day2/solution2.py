with open('input1.txt', 'r') as f:
    line = f.read().strip()

def is_invalid(num):
    
    return False

def find_invalid_digits(sequence_range, invalid_digits):
    for num in range(sequence_range[0], sequence_range[1] + 1):
        if is_invalid(num):
            invalid_digits.append(num)

invalid_digits = []
for part in line.split(','):
    start, end = map(int, part.split('-'))
    find_invalid_digits((start, end), invalid_digits)

print(sum(invalid_digits))




