from collections import defaultdict
f = open('4\input')

winning = []
mine = []

lines = []

for i, line in enumerate(f):
    str_line = line.strip()

    lines.append(1)

    winning_nums = str_line.split('|')[0].split(':')[1]
    my_nums = str_line.split('|')[1]

    winning_nums = [int(num.strip()) for num in winning_nums.split()]
    my_nums = [int(num.strip()) for num in my_nums.split()]

    winning.append(winning_nums)
    mine.append(my_nums)

answers = []

for i in range(len(winning)):
    target_nums = set(winning[i])
    picked_nums = mine[i]

    total_nums = 0

    for n in picked_nums:
        if n in target_nums:

            total_nums += 1
    
    answers.append(total_nums)

vals = [2 ** (i - 1) if i >= 1 else 0 for i in answers]

print(sum(vals)) # part 1

answers2 = []

total_scratchcards = len(lines)

for i in range(len(lines)):
    while lines[i] > 0:
        target_nums = set(winning[i])
        picked_nums = mine[i]

        total_nums = 0

        for n in picked_nums:
            if n in target_nums:
                total_nums += 1

        for j in range(1, total_nums + 1):
            if i + j < len(lines):
                lines[i + j] += 1
                total_scratchcards += 1
        
        lines[i] -= 1 


print(total_scratchcards) # part 2