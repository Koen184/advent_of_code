import re
import math


# DAY EIGHT

# PART ONE

# data = []
#
# with open('input_day8.txt') as file:
#     for line in file:
#         line = line.strip()
#         data.append(line)
#
# instruction = data[0]
# data = data[2:]
#
# mod_data = []
#
# for element in data:
#     mod_data.append([element[0:3], element[7:10], element[12:15]])
#
# for data in mod_data:
#     if data[0] == 'AAA':
#         actual = data
#     elif data[0] == 'ZZZ':
#         end = data
#
# steps = 0
# index = 0
# flag = 0
#
# while flag == 0:
#     if index == len(instruction):
#         index = 0
#
#     for element in mod_data:
#         if instruction[index] == 'R' and element[0] == actual[2]:
#             actual = element
#             steps = steps + 1
#             index = index + 1
#
#             if actual[0] == end[0]:
#                 flag = 1
#
#             break
#
#         elif instruction[index] == 'L' and element[0] == actual[1]:
#             actual = element
#             steps = steps + 1
#             index = index + 1
#
#             if actual[0] == end[0]:
#                 flag = 1
#
#             break
#
# print(steps)

# PART TWO

# data = []
#
# with open('input_day8.txt') as file:
#     for line in file:
#         line = line.strip()
#         data.append(line)
#
# instruction = data[0]
# data = data[2:]
#
# mod_data = []
#
# for element in data:
#     mod_data.append([element[0:3], element[7:10], element[12:15]])
#
# actual = []
# end = []
#
# for data in mod_data:
#     if re.match(r'..A', data[0]):
#         actual.append(data)
#     elif re.match(r'..Z', data[0]):
#         end.append(data)
#
# steps = 0
# index = 0
# flag = 0
#
# while flag == 0:
#     if index == len(instruction):
#         index = 0
#
#     for i, element_actual in enumerate(actual):
#         for element in mod_data:
#             if instruction[index] == 'R' and element[0] == element_actual[2]:
#                 actual[i] = element
#                 break
#             elif instruction[index] == 'L' and element[0] == element_actual[1]:
#                 actual[i] = element
#                 break
#
#     steps = steps + 1
#     index = index + 1
#
#     check = 0
#
#     for element_actual in actual:
#         if re.match(r'..Z', element_actual[0]):
#             check = check + 1
#             print(check)
#             print(steps)
#
#     if check == len(end):
#         flag = 1
#
# print(steps)


# PART TWO _ OPTION B -> faster

# data = []
#
# with open('input_day8.txt') as file:
#     for line in file:
#         line = line.strip()
#         data.append(line)
#
# instruction = data[0]
# data = data[2:]
#
# data_dict = {}
#
# for element in data:
#     key = element[0:3]
#     data_dict[key] = (element[0:3], element[7:10], element[12:15])
#
# actual = set()
# end = set()
#
# for key, value in data_dict.items():
#     if key.endswith('A'):
#         actual.add(key)
#     elif key.endswith('Z'):
#         end.add(key)
#
# steps = 0
# index = 0
#
# while True:
#     if index == len(instruction):
#         print(steps)
#         index = 0
#
#     for key in list(actual):
#         next_key = data_dict[key][2] if instruction[index] == 'R' else data_dict[key][1]
#         if next_key in data_dict:
#             actual.remove(key)
#             actual.add(next_key)
#
#     steps += 1
#     index += 1
#
#     if sum(1 for key in actual if key.endswith('Z')) == len(end):
#         break
#
# print(steps)


# PART TWO - FINAL - least common multiple

data = []

with open('input_day8.txt') as file:
    for line in file:
        line = line.strip()
        data.append(line)

instruction = data[0]
data = data[2:]

mod_data = []

for element in data:
    mod_data.append([element[0:3], element[7:10], element[12:15]])

actual = []
end = []

for data in mod_data:
    if re.match(r'..A', data[0]):
        actual.append(data)
    elif re.match(r'..Z', data[0]):
        end.append(data)

lcm_values = []

for element_actual in actual:
    steps = 0
    index = 0
    flag = 0

    while flag == 0:
        if index == len(instruction):
            index = 0

        for element in mod_data:
            if instruction[index] == 'R' and element[0] == element_actual[2]:
                element_actual = element
                break
            elif instruction[index] == 'L' and element[0] == element_actual[1]:
                element_actual = element
                break

        steps = steps + 1
        index = index + 1

        check = 0

        if element_actual in end:
            lcm_values.append(steps)
            flag = 1

print(lcm_values)
print(math.lcm(*lcm_values))
