import numpy as np

# DAY NINE

# PART ONE

# data = []
#
# with open('input_day9.txt') as file:
#     for line in file:
#         line = line.strip()
#         data.append(line)
#
# values_to_sum = []
#
# for line in data:
#     value_list = [int(symbol) for symbol in line.split(' ')]
#     value_list.append(0)
#     value_table = np.array(value_list)
#
#     add_row = []
#     for i in range(len(value_list)):
#         add_row.append(0)
#
#     flag = 0
#     row = 0
#
#     while flag == 0:
#         value_table = np.vstack([value_table, add_row])
#
#         check = 0
#         for value in (value_table[row, :]):
#             if value != 0:
#                 check += 1
#
#         if check >= 1:
#             for i in range(row + 1, len(value_list) - 1):
#                 value_table[row + 1][i] = value_table[row][i] - value_table[row][i - 1]
#
#             row += 1
#         else:
#             for i in range(np.shape(value_table)[0] - 3, -1, -1):
#                 value_table[i][np.shape(value_table)[1] - 1] = value_table[i][np.shape(value_table)[1] - 2] + value_table[i + 1][np.shape(value_table)[1] - 1]
#
#             values_to_sum.append(value_table[0][np.shape(value_table)[1] - 1])
#             flag = 1
#
# print(values_to_sum)
# print(len(values_to_sum))
# print(sum(values_to_sum))


# PART TWO

data = []

with open('input_day9.txt') as file:
    for line in file:
        line = line.strip()
        data.append(line)

values_to_sum = []

for line in data:
    value_list = [int(symbol) for symbol in line.split(' ')]
    value_list.append(0)
    value_table = np.array(value_list)

    add_row = []
    for i in range(len(value_list)):
        add_row.append(0)

    flag = 0
    row = 0

    while flag == 0:
        value_table = np.vstack([value_table, add_row])

        check = 0
        for value in (value_table[row, :]):
            if value != 0:
                check += 1

        if check >= 1:
            for i in range(row + 1, len(value_list) - 1):
                value_table[row + 1][i] = value_table[row][i] - value_table[row][i - 1]

            row += 1
        else:
            value_table = np.fliplr(value_table)
            value_table = value_table[:-1, :]

            start_index = 0
            last_row = value_table[-2, 1:]
            for value in last_row:
                if value != 0:
                    start_index += 1
                else:
                    break

            for i in range(np.shape(value_table)[0] - 2, -1, -1):
                value_table[i][0] = value_table[i][start_index] - value_table[i + 1][0]
                start_index += 1

            values_to_sum.append(value_table[0][0])
            flag = 1

print(values_to_sum)
print(len(values_to_sum))
print(sum(values_to_sum))
