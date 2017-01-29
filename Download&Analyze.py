import urllib.request, urllib.parse
import glob
import os
import sys
from bs4 import BeautifulSoup
import glob
url = input("[+] Enter the url 'http://www.pgnmentor.com/files.html': ")
download_path = input("[+] Enter the download path in full: ")

try:
    # mask as browser
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}

    i = 0

    request = urllib.request.Request(url, None, headers)
    html = urllib.request.urlopen(request)
    soup = BeautifulSoup(html.read(), 'html.parser') # to parse the website

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

path = download_path + "*.pgn"
white = 0
black = 0
games = 0
for filename in glob.glob(path):
    print("current file is being analyzed: " + filename)
    print("=" * 85)
    with open(filename, 'r') as f:
        for line in f:
            if 'result "1-0"' in line.lower():
                white += 1
            if 'result "0-1"' in line.lower():
                black += 1
            if 'event' in line.lower():
                games += 1
    draw = games - (black + white)
    print("This file has " + str(games) + " games being analyzed.")
    print("White has won " + str(white) + " games/ " + str(100 * float(white)/float(games)) + "%")
    print("Black has won " + str(black) + " games/ " + str(100 * float(black)/float(games)) + "%")
    print("There has been " + str(draw) + " draws/ " + str(100 * float(draw)/float(games)) + "%")



