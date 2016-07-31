firom crawl import *

"""
enter of the whole program
"""

if __name__ == '__main__':
    url = raw_input("input url:")
    music_url, music = getMusicInfo(url)
    getMusic(music_url, music)
