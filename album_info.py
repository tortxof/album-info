#! /usr/bin/env python3

import sys
import json

import requests
from bs4 import BeautifulSoup

def get_info(url):
    '''Returns dict of album info given url of album on metal-archives.com.'''
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    num_tracks = (len(soup.select("table.display.table_lyrics tr")) - 1) // 2
    album = soup.select("h1.album_name a")[0].text.strip()
    artist = soup.select("h2.band_name a")[0].text.strip()
    titles = []
    for i in range(num_tracks):
        title = soup.select("table.display.table_lyrics tr")[i * 2].select("td")[1].text.strip()
        titles.append(title)
    return {'album': album, 'artist': artist, 'titles': titles}

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        print(json.dumps(
            get_info(url),
            indent = 2
            ))
    else:
        print('Usage: ' + sys.argv[0] + ' metal-archives_url')
