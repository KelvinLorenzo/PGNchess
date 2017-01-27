# Script to read all .pgn files and output its content
# As of right now, must pre determine the path
import sys
import glob

path = '/users/kelvin/desktop/test/*.pgn'
files = glob.glob(path)
for pgn in files:
    print("current file is being analyzed: " + pgn)
    print('=' * 85)
    with open(pgn) as f:
        sys.stdout.write(f.read())