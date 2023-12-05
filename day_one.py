# DAY ONE

import re


values_list = []
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

with open('input_day1.txt') as lines:
    for line in lines:
        for number in numbers:
            line = re.sub(number, number[0] + digits[numbers.index(number)] + number[2:], line)

        print(line)
        elements = []

        for element in line:
            if element.isdigit():
                elements.append(element)

        values_list.append(int(elements[0] + elements[-1]))
        print(int(elements[0] + elements[-1]))

final_sum = sum(values_list)
print(final_sum)

