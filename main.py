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
max_mirror_tries = 10
ydl_opts = {} # options https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L129-L279

def get_stream_url(season, episode, mirror):
    # construct url
    # http://kinox.to/aGET/Mirror/Charmed-Zauberhafte_Hexen&Hoster=30&Mirror=1&Season=2&Episode=1

    payload = {
        "Mirror": mirror,
        "Hoster": hoster_id,
        "Season": season,
        "Episode": episode
    }

    r = requests.get(mirror_api + series_id, params=payload)

    if len(r.content) == 0:
        return None

    r_html = r.json()["Stream"]

    soup = BeautifulSoup(r_html, 'html.parser')

    return soup.a.get('href')

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for episode in range(episode_start, episode_end+1):
        for mirror in range(1, max_mirror_tries+1):
            stream_url = get_stream_url(season, episode, mirror)

            if stream_url == None:
                if mirror == max_mirror_tries:
                    print("skipping season", season, "episode", episode)
                continue

            ydl_return = ydl.download([stream_url])

            if ydl_return == 0:
                break
            else:
                print("ydl return:", ydl_return)
