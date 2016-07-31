import sys
import urllib
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

"""
This script aims to parse the music url from changba url and download the music
to directory export_files.
"""

def getMusicInfo(url):
    html = requests.get(url, timeout=1).text
    soup = BeautifulSoup(html, 'html.parser')
    workid = soup.find('body')['data-workid']
    path = '../export_files/' + soup.find('div', class_ = 'title').text + '.mp3'
    return 'http://qiniuuwmp3.changba.com/' + workid + '.mp3', path

def getMusic(url, music_name):
    urllib.urlretrieve(url, music_name)

if __name__ == '__main__':
    url = raw_input("input url:")
    music_url, path = getMusicUrl(url)
    getMusic(music_url, path)
