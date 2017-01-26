# Script to download all .pgn files to users choice of directory
# Input http://www.pgnmentor.com/files.html
# Input a directory, ex.  /users/kelvin/desktop/pgnfolder/

import urllib.request, urllib.error, urllib.parse
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
    soup = BeautifulSoup(html.read()) # to parse the website

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

    print("\n[*] Downloaded {} files".format(i+1 - 1))
    input("[+] Enter any key to exit...")

except KeyboardInterrupt:
    print("[*] Exiting...")
    sys.exit(1)