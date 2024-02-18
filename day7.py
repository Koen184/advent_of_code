# DAY SEVEN

def remove_duplicates(cards):
    seen = {}
    results = []

    for sublist in cards:
        symbol = sublist[0]
        value = sublist[1]

        if symbol not in seen:
            seen[symbol] = value
            results.append(sublist)

    return results


def custom_order_index(character, order):
    return order.index(character) if character in order else float('inf')


with open('input_day7.txt') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    lines = [line.split(' ') for line in lines]

for line in lines:
    count_list = []

    for character in line[0]:
        count = line[0].count(character)
        count_list.append([character, count])

    count_list = remove_duplicates(count_list)
    line.append(count_list)

# PART TWO LOOP - START

for line in lines:
    for sublist in line[2]:
        key = ''

        if 'J' in sublist and len(line[2]) != 1:
            line_to_sort = [element for element in line[2] if element[0] != 'J']
            sorted_line = sorted(line_to_sort, key=lambda x: x[1], reverse=True)
            key = sorted_line[0][0]
            value = sublist[1]

        for sublist_2 in line[2]:
            if key != '' and sublist_2[0] == key:
                sublist_2[1] = sublist_2[1] + value
                line[2].remove(['J', value])

# PART TWO LOOP - END

five_of_kind = []
four_of_kind = []
full_house = []
three_of_kind = []
two_pair = []
one_pair = []
high_card = []

flag = 0

for line in lines:
    if len(line[2]) == 1:
        five_of_kind.append(line)

    elif len(line[2]) == 2:
        for sublist in line[2]:
            if sublist[1] == 4:
                four_of_kind.append(line)
                break
            elif sublist[1] == 3:
                full_house.append(line)
                break

    elif len(line[2]) == 3:
        for sublist in line[2]:
            if sublist[1] == 3:
                three_of_kind.append(line)
                break
            elif sublist[1] == 2:
                two_pair.append(line)
                break

    elif len(line[2]) == 4:
        one_pair.append(line)

    elif len(line[2]) == 5:
        high_card.append(line)

types_of_hands = [high_card, one_pair, two_pair, three_of_kind, full_house, four_of_kind, five_of_kind]

full_results = []
final_score = 0

# PART ONE ORDER
# order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# PART TWO ORDER
order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

for hand in types_of_hands:
    sorted_hand = sorted(hand, key=lambda x: [custom_order_index(c, order) for c in x[0]])
    full_results = full_results + sorted_hand

for value, record in enumerate(full_results):
    final_score = final_score + (int(record[1]) * (value + 1))

print(final_score)
