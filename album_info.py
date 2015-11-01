#! /usr/bin/env python3

import sys
import json

import requests
from bs4 import BeautifulSoup

def song_rows(tag):
    if tag.get('class'):
        return tag.get('class')[0] in ['even', 'odd']
    else:
        return False

def get_info(url):
    '''Returns dict of album info given url of album on metal-archives.com.'''
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.select("table.display.table_lyrics")[0].find_all(song_rows)
    album = soup.select("h1.album_name a")[0].text.strip()
    artist = soup.select("h2.band_name a")[0].text.strip()
    tracks = []
    for i in rows:
        track = i.select("td")[1].text.strip()
        tracks.append(track)
    return {'album': album, 'artist': artist, 'tracks': tracks}

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        print(json.dumps(
            get_info(url),
            indent = 2
            ))
    else:
        print('Usage: ' + sys.argv[0] + ' metal-archives_url')
