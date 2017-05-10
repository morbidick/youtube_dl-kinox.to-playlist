#!/usr/bin/env python3

import youtube_dl
import requests
from bs4 import BeautifulSoup

mirror_api = "http://kinox.to/aGET/Mirror/"
series_id = "Charmed-Zauberhafte_Hexen"
hoster_id = 30 #streamcloud.eu
season = 3
episode_start = 1
episode_end = 22
episode_stream_urls = []

def get_stream_url(season, episode):
    # construct url
    # http://kinox.to/aGET/Mirror/Charmed-Zauberhafte_Hexen&Hoster=30&Mirror=1&Season=2&Episode=1

    payload = {
        "Hoster": hoster_id,
        "Season": season,
        "Episode": episode
    }

    r = requests.get('http://kinox.to/aGET/Mirror/' + series_id, params=payload)
    r_html = r.json()["Stream"]

    soup = BeautifulSoup(r_html, 'html.parser')

    return soup.a.get('href')

for episode in range(episode_start, episode_end):
    episode_stream_urls.append(get_stream_url(season, episode))

# options https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L129-L279
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(episode_stream_urls)
