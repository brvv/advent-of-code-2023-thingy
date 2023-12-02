
def side_sum(cal : str):
    
    digits = [num for num in cal if num in '123456789']

    return int(digits[0] + digits[-1])

file = open('sample1', 'r')

total = 0

# part 1

for line in file:
    total += side_sum(line)

print(total) # part 1


# part 2

nums_dict = {'one' : '1',
'two' : '2',
'three' : '3',
'four' : '4',
'five' : '5',
'six' : '6',
'seven' : '7',
'eight' : '8',
'nine' : '9'}

def is_number(line, i):
    for num in nums_dict:
        if len(line) - i >= len(num) and line[i : i + len(num)] == num:
            return nums_dict[num]
    return None

def get_num(line : str, i):
    if line[i] in '123456789':
        return line[i]
    return is_number(line, i)

def get_first_num(line : str):
    for i in range(len(line)):
        num = get_num(line, i)
        if num is None:
            continue
        return num


def get_last_num(line : str):
    for i in range(len(line) - 1, -1, -1):
        num = get_num(line, i)
        if num is None:
            continue
        return num

total_2 = 0
file.seek(0)

for line in file:
    first_num = get_first_num(line)
    last_num = get_last_num(line)

    print(line, first_num, last_num)

    total_2 += int(first_num + last_num)

print(total_2)
