import requests
import sys
import bs4
import bz2

SITE = 'https://database.lichess.org/'
LINK = 'standard/lichess_db_standard_rated_2017-03.pgn.bz2'
r = requests.get(SITE)
if not r.ok:
    sys.exit()
soup = bs4.BeautifulSoup(r.text, 'lxml')
#print(soup)
file = soup.find_all('a', href=LINK)
chess_url = next(iter(file)).get('href')
url = SITE + chess_url
r = requests.get(url)
r = bz2.decompress(r.content)
soup = bs4.BeautifulSoup(r.text, 'lxml')

with open('data.pgn', 'w') as f:
    f.write(soup.get_text())

#print(help(r))
#print(type(r))
#print(type(bz2.decompress(r.content)))
