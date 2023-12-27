# DAY THREE

import numpy as np


# FUNCTIONS - PART ONE

def check_symbols(array, num, list_of_nums):
    size_clip = list(array.shape)
    elements = size_clip[0] * size_clip[1] - len(num)

    count_dots = np.count_nonzero(array == '.')

    if elements != count_dots:
        list_of_nums.append(int(num))


# PART ONE

# with open('input_day3.txt') as file:
#     lines = file.readlines()
#     lines = [line.strip() for line in lines]
#     lines = [(line + '.') for line in lines]
#     data = np.array([list(line) for line in lines])
#
# size = list(data.shape)
# numbers = []
#
# for i in range(0, size[0]):
#     number = ''
#
#     for j in range(0, size[1]):
#         if data[i, j].isdigit():
#             number = number + data[i, j]
#         else:
#             if not number == '':
#                 if (j - len(number) - 1) <= 0 and (i - 1) <= 0 and number != '':
#                     check_data = data[0:(i + 2), 0:(j + 1)]
#                     check_symbols(check_data, number, numbers)
#                     number = ''
#                 elif (j - len(number) - 1) <= 0 and number != '':
#                     check_data = data[(i - 1):(i + 2), 0:(j + 1)]
#                     check_symbols(check_data, number, numbers)
#                     number = ''
#                 elif (i - 1) <= 0 and number != '':
#                     check_data = data[0:(i + 2), (j - len(number) - 1):(j + 1)]
#                     check_symbols(check_data, number, numbers)
#                     number = ''
#                 else:
#                     check_data = data[(i - 1):(i + 2), (j - len(number) - 1):(j + 1)]
#                     check_symbols(check_data, number, numbers)
#                     number = ''
#
# print(sum(numbers))


# FUNCTIONS - PART TWO


def extract_numbers(array):
    numbers = []
    for row in array:
        num_str = ''
        for char in row:
            if char.isdigit():
                num_str += char
            elif num_str:
                numbers.append(int(num_str))
                num_str = ''
        if num_str:
            numbers.append(int(num_str))
    return numbers


def check_numbers(array, ratios):
    rows = []

    for row in array:
        rows.append(list(row))

    for row in rows:
        if row[2].isdigit() and row[4].isdigit():
            if row[3].isdigit():
                row[0] = '.'
                row[6] = '.'
            else:
                continue
        elif row[2].isdigit() and row[3].isdigit():
            row[0] = '.'
            row[5] = '.'
            row[6] = '.'
        elif row[2].isdigit():
            row[5] = '.'
            row[6] = '.'
        elif row[4].isdigit() and row[3].isdigit():
            row[0] = '.'
            row[1] = '.'
            row[6] = '.'
        elif row[4].isdigit():
            row[0] = '.'
            row[1] = '.'
        else:
            row[0] = '.'
            row[1] = '.'
            row[5] = '.'
            row[6] = '.'

    numbers = extract_numbers(rows)

    if len(numbers) != 2:
        return
    else:
        ratios.append(numbers[0] * numbers[1])


# PART TWO

with open('input_day3.txt') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    lines = [('.' + line + '.') for line in lines]
    data = np.array([list(line) for line in lines])

size = list(data.shape)
gear_ratios = []

for i in range(0, size[0]):
    for j in range(0, size[1]):
        if data[i, j] == '*':
            check_data = data[(i - 1):(i + 2), (j - 3):(j + 4)]
            check_numbers(check_data, gear_ratios)

print(sum(gear_ratios))
