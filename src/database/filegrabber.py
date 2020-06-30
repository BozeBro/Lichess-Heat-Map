def file_grab(link='standard/lichess_db_standard_rated_2013-01.pgn.bz2'):
    import requests
    import sys
    import bs4
    import bz2
    SITE = 'https://database.lichess.org/'
    LINK = link

    r = requests.get(SITE)
    if not r.ok:
        sys.exit()
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    file = soup.find_all('a', href=LINK)
    chess_url = next(iter(file)).get('href')

    url = SITE + chess_url
    r = requests.get(url)
    r = bz2.decompress(r.content)
    soup = bs4.BeautifulSoup(r, 'lxml')

    file = "data.pgn"
    with open(file, 'w') as f:
        f.write(soup.get_text())


if __name__ == '__main__':
    file_grab()
