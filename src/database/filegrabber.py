def file_grab(site='https://database.lichess.org/', link='standard/lichess_db_standard_rated_2014-07.pgn.bz2'):
    """
    Gets the chess file from the database.lichess site.
    :parameter
    ---------
    SITE
        The website
    link
        href link of the desired pgn file. 
    file_grab will grab the file off the site and write the file into a data.pgn file
    """
    import requests
    import sys
    import bs4
    import bz2
    LINK = link
    SITE = site
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
    FILE = "data.pgn"
    with open(FILE, 'w') as f:
        f.write(soup.get_text())


if __name__ == '__main__':
    file_grab()
