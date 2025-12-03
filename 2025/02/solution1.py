with open('input1.txt', 'r') as f:
    line = f.read().strip()


def find_invalid_digits(sequence_range,invalid_digits):
    for digits in range(sequence_range[0],sequence_range[1]+1):
        digits = str(digits)
        if len(digits)%2 == 0:
            if digits[:len(digits)//2] == digits[len(digits)//2:]:
                invalid_digits.append(int(digits))
                

invalid_digits = []
for part in line.split(','):
    start, end = map(int, part.split('-'))
    find_invalid_digits((start,end),invalid_digits)

print(sum(invalid_digits))




