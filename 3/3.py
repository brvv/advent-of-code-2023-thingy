import re
from collections import defaultdict
from functools import reduce
file = open('./3/input')

digits = set('0123456789')

gears_dict = defaultdict(list)

def has_adjacent_symbol(matrix, row_i, col_y):
    for dx in range(-1, 2, 1):
        for dy in range(-1, 2, 1):
            n_row_i = row_i + dx
            n_col_i = col_y + dy

            if 0 <= n_row_i < len(matrix) and 0 <= n_col_i < len(matrix[0]):
                val = matrix[n_row_i][n_col_i]

                if val != '.' and val not in digits:
                    return True
    return False

def get_adjacent_gears(matrix, row_i, col_y):
    adjacent_gears = []

    for dx in range(-1, 2, 1):
        for dy in range(-1, 2, 1):
            n_row_i = row_i + dx
            n_col_i = col_y + dy

            if 0 <= n_row_i < len(matrix) and 0 <= n_col_i < len(matrix[0]):
                val = matrix[n_row_i][n_col_i]

                if val == '*':
                    adjacent_gears.append((n_row_i, n_col_i))
    return adjacent_gears

def get_full_number(row, col_y):
    ans = []

    starting = row[col_y]

    dy = -1

    while col_y + dy >= 0 and row[col_y + dy] in digits:
        ans.append(row[col_y + dy])
        dy -= 1
    
    ans = ans[::-1]

    dy = 0

    while col_y + dy < len(row) and row[col_y + dy] in digits:
        ans.append(row[col_y + dy])
        dy += 1

    return ''.join(ans)


def get_numbers_adjacent_to_symbol(matrix):
    ans = []

    for row_i in range(len(matrix)):
        row = matrix[row_i]

        col_i = 0

        while col_i < len(row):
            if row[col_i] not in digits:
                col_i += 1
                continue

            has_adjacent = has_adjacent_symbol(matrix, row_i, col_i)
            
            if has_adjacent and row[col_i] in digits:
                val = get_full_number(row, col_i)
                ans.append(val)

                gears_added_to = set()

                while col_i < len(row) and row[col_i] in digits:

                    adjacent_gears = get_adjacent_gears(matrix, row_i, col_i)

                    for gear in adjacent_gears:
                        if gear not in gears_added_to:
                            gears_dict[gear].append(int(val))
                            gears_added_to.add(gear)

                    col_i += 1
            else:
                col_i += 1
    return ans

matrix = []

for line in file:
    matrix.append(line.strip())

ans = get_numbers_adjacent_to_symbol(matrix)

print(sum([int(i) for i in ans]))

ans = 0

for gear_coords, gear_nums in gears_dict.items():
    if len(gear_nums) == 2:
        ans += gear_nums[0] * gear_nums[1]

print(ans)