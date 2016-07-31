import sys
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
    music = soup.find('div', class_ = 'title').text + '.mp3'
    return 'http://qiniuuwmp3.changba.com/' + workid + '.mp3', music

def getMusic(url, music):
    with open('../export_files/' + music, 'wb') as f:
        print "Downloading " + music
        response = requests.get(url, stream=True)
        length = response.headers.get('content-length')
        if length is None:
            f.write(response.content)
        else:
            dl = 0
            length = int(length)
            for data in response.iter_content(length/100):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / length)
                sys.stdout.write('\r[%s%s]%s%%' % 
                        ('=' * done, ' ' * (50-done), str(2 * done)))
                sys.stdout.flush()
            print '\n'

if __name__ == '__main__':
    url = raw_input("input url:")
    music_url, music = getMusicInfo(url)
    getMusic(music_url, music)
