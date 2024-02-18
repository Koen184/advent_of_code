# DAY TWO

import re

# PART ONE

# red_cubes = 12
# green_cubes = 13
# blue_cubes = 14
#
# number_game = 0
# sum_games = 0
#
# with open('input_day2.txt') as lines:
#     for line in lines:
#         number_game = number_game + 1
#         flag = 0
#
#         line = line[line.index(':') + 1:]
#         line_split = line.split(';')
#
#         for game in line_split:
#             game = game.split(',')
#
#             for score in game:
#                 if 'red' in score:
#                     if not int((re.findall(r'\d+', score))[0]) < 13:
#                         flag = 1
#                         break
#                 if 'green' in score:
#                     if not int((re.findall(r'\d+', score))[0]) < 14:
#                         flag = 1
#                         break
#                 if 'blue' in score:
#                     if not int((re.findall(r'\d+', score))[0]) < 15:
#                         flag = 1
#                         break
#
#         if flag == 0:
#             sum_games = sum_games + number_game
#
# print(sum_games)

# PART TWO

powers = []

with open('input_day2.txt') as lines:
    for line in lines:
        red_max = 1
        green_max = 1
        blue_max = 1

        line = line[line.index(':') + 1:]
        line_split = line.split(';')

        for game in line_split:
            game = game.split(',')

            for score in game:
                if 'red' in score:
                    if int((re.findall(r'\d+', score))[0]) > red_max:
                        red_max = int((re.findall(r'\d+', score))[0])
                if 'green' in score:
                    if int((re.findall(r'\d+', score))[0]) > green_max:
                        green_max = int((re.findall(r'\d+', score))[0])
                if 'blue' in score:
                    if int((re.findall(r'\d+', score))[0]) > blue_max:
                        blue_max = int((re.findall(r'\d+', score))[0])

        powers.append(red_max * green_max * blue_max)

print(sum(powers))
