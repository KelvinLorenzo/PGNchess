# import os
# directory = '/users/kelvin/desktop/test/'
# for root, dirs, filenames in os.walk(directory):
#     for f in filenames:
#         log = open(os.path.join(root, f), 'r')
#
#         white = 0
#         black = 0
#         games = 0
#         if 'result "1-0"' in f.lower():
#             white += 1
#         if 'result "0-1"' in f.lower():
#             black += 1
#         if 'event' in f.lower():
#             games += 1
#         draw = games - (black + white)
# # Outputs the number of games analyzed per pgn file
#         print("This file has " + str(games) + " games being analyzed.")
# # Outputs the number of games won by white/black/draw and percentage won for each
#         print("White has won " + str(white) + " games/ " + str(100 * float(white)/float(games)) + "%")
#         print("Black has won " + str(black) + " games/ " + str(100 * float(black)/float(games)) + "%")
#         print("There has been " + str(draw) + " draws/ " + str(100 * float(draw)/float(games)) + "%")


import sys
import glob
import fileinput
path = '/users/kelvin/desktop/test/*.pgn'
files = glob.glob(path)
white = 0
black = 0
games = 0
draw = games - (black + white)
for pgn in files:
    pgn = open(pgn, "w")
    # pgn = fileinput.input(pgn)
    print("current file being analyzed: " + pgn)
    print('=' * 85)
    if 'result' "1-0" in pgn:
        white += 1
    if 'result "0-1"' in pgn:
        black += 1
    if 'event' in pgn:
        games += 1

# Outputs the number of games analyzed per pgn file
    print("This file has " + str(games) + " games being analyzed.")
# # Outputs the number of games won by white/black/draw and percentage won for each
# print("White has won " + str(white) + " games/ " + str(100 * white/games) + "%")
# print("Black has won " + str(black) + " games/ " + str(100 * black/games) + "%")
# print("There has been " + str(draw) + " draws/ " + str(100 * draw/games) + "%")

    # with open(pgn) as f:
    # white = 0
    # black = 0
    # games = 0
    #     if 'result "1-0"' in content.lower():
    #         white += 1
    #     if 'result "0-1"' in content.lower():
    #         black += 1
    #     if 'event' in content.lower():
    #         games += 1
    #
    #     draw = games - (black + white)
    # # Outputs the number of games analyzed per pgn file
    #     print("This file has " + str(games) + " games being analyzed.")
    # Outputs the number of games won by white/black/draw and percentage won for each
    # print("White has won " + str(white) + " games/ " + str(100 * white/games) + "%")
    # print("Black has won " + str(black) + " games/ " + str(100 * black/games) + "%")
    # print("There has been " + str(draw) + " draws/ " + str(100 * draw/games) + "%")
    # sys.stdout.write(f.read())