# DAY FOUR

list_points = []
number_of_cards = []

with open('input_day4.txt') as lines:
    num_lines = sum(1 for line in lines if line.rstrip())
    number_of_cards = [1] * num_lines

with open('input_day4.txt') as lines:
    game = 0

    for line in lines:
        line = line[line.index(':') + 1:]
        line = line.strip()
        line_split = line.split(' | ')

        numbers_you_have = line_split[0].split(' ')
        winning_numbers = line_split[1].split(' ')

        numbers_you_have = list(filter(None, numbers_you_have))
        winning_numbers = list(filter(None, winning_numbers))

        print(numbers_you_have, winning_numbers)

        points = 0

        for element in numbers_you_have:
            if element in winning_numbers:
                points = points + 1

        list_points.append(points)

        if points != 0:
            add_cards = [1] * points

            for i in range(0, number_of_cards[game]):
                flag = 1

                for value in add_cards:
                    number_of_cards[game + flag] = number_of_cards[game + flag] + value
                    flag = flag + 1

        game = game + 1

final_score = 0

for value in list_points:
    value = int(value)
    if value != 0:
        final_score = final_score + (2 ** (int(value)-1))

# print(final_score)

print(number_of_cards)
print(sum(number_of_cards))


