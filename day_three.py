# DAY THREE

import numpy as np


def check_symbols(array, num, list_of_nums):
    size_clip = list(array.shape)
    elements = size_clip[0] * size_clip[1] - len(num)

    count_dots = np.count_nonzero(array == '.')

    # print(elements, count_dots)
    # print(array)

    if elements != count_dots:
        list_of_nums.append(int(num))
        print('INPUT: ', num)


with open('input_day3.txt') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    data = np.array([list(line) for line in lines])

print(data)

size = list(data.shape)
numbers = []

for i in range(0, size[0]):
    number = ''

    for j in range(0, size[1]):
        if data[i, j].isdigit():
            number = number + data[i, j]
            print(number)
        else:
            if not number == '':
                if (j - len(number) - 1) <= 0 and (i - 1) <= 0 and number != '':
                    check_data = data[0:(i + 2), 0:(j + 1)]
                    check_symbols(check_data, number, numbers)
                    number = ''
                    print(check_data)
                elif (j - len(number) - 1) <= 0 and number != '':
                    check_data = data[(i - 1):(i + 2), 0:(j + 1)]
                    check_symbols(check_data, number, numbers)
                    number = ''
                    print(check_data)
                elif (i - 1) <= 0 and number != '':
                    check_data = data[0:(i + 2), (j - len(number) - 1):(j + 1)]
                    check_symbols(check_data, number, numbers)
                    number = ''
                    print(check_data)
                else:
                    check_data = data[(i - 1):(i + 2), (j - len(number) - 1):(j + 1)]
                    check_symbols(check_data, number, numbers)
                    number = ''
                    print(check_data)


print(numbers)
print(sum(numbers))
print(len(numbers))

