# DAY SIX

import re

# PART ONE

# ways_to_win = []
#
# with open('input_day6.txt') as file:
#     lines = file.readlines()
#     values = []
#
#     for line in lines:
#         values.append(re.findall(r'\d+', line))
#
#     times = values[0]
#     distances = values[1]
#
#     for i, time in enumerate(times):
#         count = 0
#
#         for start in range(0, (int(time) + 1)):
#             if (int(time) - start) * start > int(distances[i]):
#                 count = count + 1
#
#         ways_to_win.append(count)
#
# final_score = 1
#
# for value in ways_to_win:
#     final_score = final_score * value
#
#
# print(final_score)

# PART TWO

with open('input_day6.txt') as file:
    lines = file.readlines()
    values = []

    for line in lines:
        values.append(re.findall(r'\d+', line))

    time = ''
    for value in values[0]:
        time = time + value
    time = int(time)

    distance = ''
    for value in values[1]:
        distance = distance + value
    distance = int(distance)

    count = 0
    for start in range(0, time + 1):
        if (time - start) * start > distance:
            count = count + 1

print(count)
