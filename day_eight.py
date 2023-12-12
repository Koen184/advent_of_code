# DAY EIGHT

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

for data in mod_data:
    if data[0] == 'AAA':
        actual = data
    elif data[0] == 'ZZZ':
        end = data

steps = 0
index = 0
flag = 0

while flag == 0:
    if index == len(instruction):
        index = 0

    for element in mod_data:
        if instruction[index] == 'R' and element[0] == actual[2]:
            actual = element
            steps = steps + 1
            index = index + 1

            if actual[0] == end[0]:
                flag = 1

            break

        elif instruction[index] == 'L' and element[0] == actual[1]:
            actual = element
            steps = steps + 1
            index = index + 1

            if actual[0] == end[0]:
                flag = 1

            break

print(steps)
