# Currently only analyzes a single/pre specified file, in a pre specified directory
jabber = open("/Users/kelvin/desktop/test1/\Moscow2011.pgn")
white = 0
black = 0
games = 0
for line in jabber:
    if 'result "1-0"' in line.lower():
        white += 1
    if 'result "0-1"' in line.lower():
        black += 1
    if 'event' in line.lower():
        games += 1
draw = games - (black + white)
# Outputs the number of games analyzed per pgn file
print("This file has " + str(games) + " games being analyzed.")
# Outputs the number of games won by white/black/draw and percentage won for each
print("White has won " + str(white) + " games/ " + str(100 * float(white)/float(games)) + "%")
print("Black has won " + str(black) + " games/ " + str(100 * float(black)/float(games)) + "%")
print("There has been " + str(draw) + " draws/ " + str(100 * float(draw)/float(games)) + "%")