import urllib.request, urllib.parse
import os
import sys
from bs4 import BeautifulSoup
import pgn
from statistics import median, mean
import numpy as np
url = input("[+] Enter the url 'http://www.pgnmentor.com/files.html': ")
download_path = input("[+] Enter the download path in full: ")

try:
    # mask as browser
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}

    i = 0

    request = urllib.request.Request(url, None, headers)
    html = urllib.request.urlopen(request)
    soup = BeautifulSoup(html.read(), 'html.parser')  # to parse the website

    # find <a> tags with href
    for tag in soup.findAll('a', href=True):
        tag['href'] = urllib.parse.urljoin(url, tag['href'])

        # Pulls the extention with (splittext) from the url(basename) splittext used to split the extention [1]
        if os.path.splitext(os.path.basename(tag['href']))[1] == '.pgn':
            current = urllib.request.urlopen(tag['href'])
            print("\n[*] Downloading: {}".format(os.path.basename(tag['href'])))

            f = open(download_path + "\\" + os.path.basename(tag['href']), 'wb')
            f.write(current.read())
            f.close()
            i += 1
except KeyboardInterrupt:
    print("[*] Exiting...")
    sys.exit(1)

print("\n[*] Downloaded {} files".format(i+1 - 1))
input("Enter any key to perform the stats: ")
spath = download_path
for roots, dirs, files in os.walk(spath):
    files = [f for f in files if not f[0] == '.']  # skips hidden files in directory
    for fName in files:
        white = 0
        black = 0
        games = 0
        print("\n[*] Current file being analyzed: " + fName)
        print("=" * 85)
        with open(os.path.join(roots, fName), 'r') as dlFile:
            for content in dlFile:
                if 'result "1-0"' in content.lower():
                    white += 1
                if 'result "0-1"' in content.lower():
                    black += 1
                if 'event' in content.lower():
                    games += 1
        draw = games - (black + white)
        print("This file has " + str(games) + " games being analyzed.")
        print("White has won " + str(white) + " games/ " + str(100 * float(white)/float(games)) + "%")
        print("Black has won " + str(black) + " games/ " + str(100 * float(black)/float(games)) + "%")
        print("There has been " + str(draw) + " draws/ " + str(100 * float(draw)/float(games)) + "%")
        with open(os.path.join(roots, fName)) as cFile:
            aGames = pgn.loads(cFile.read())
            countList = []
            for game in aGames:
                counts = "{} vs {}, {} moves.".format(game.white, game.black, len(game.moves))
                print(counts)
                countList += [len(game.moves)]
            print("The min value of moves for all games in " + fName + " = {}".format(min(countList)))
            print("The median value of moves for all games in " + fName + " = {}".format(median(countList)))
            print("The median value of moves for all games in " + fName + " = {}".format(mean(countList)))
            print("The max value of moves for all games in " + fName + " = {}".format(max(countList)))
            print("The 50th percentile value for moves in " + fName + " =  {}".format(np.percentile(countList, 50)))
            print("The 75th percentile value for moves in " + fName + " =  {}".format(np.percentile(countList, 75)))
            print("The 90th percentile value for moves in " + fName + " =  {}".format(np.percentile(countList, 90)))
            print("The 95th percentile value for moves in " + fName + " =  {}".format(np.percentile(countList, 95)))
            print("The 99th percentile value for moves in " + fName + " =  {}".format(np.percentile(countList, 99)))



