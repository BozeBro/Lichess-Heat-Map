import json


def game_search(file='data.pgn'):
    """
    Iterates through the PGN file

    :parameter
    ---------
    file (optional)
        The certain data file with the chess game data. File has to be a .PGN. Set to data.pgn

    cur_game acts as an iterator that iterates through the games in the pgn file
    """

    import chess.pgn
    from collections import defaultdict, Counter

    with open(file) as notated:
        cur_game = chess.pgn.read_game(notated)
        # Iterator to go through data file
        squares = defaultdict(Counter)
        # Container of each square and how many times a piece moves to that square
        while cur_game:

            try:
                wrank = int(cur_game.headers["WhiteElo"])
            except ValueError:
                # Handles "?" elo
                wrank = 1500
            try:
                brank = int(cur_game.headers["BlackElo"])
            except ValueError:
                # Handles "?" elo
                brank = 1500

            number = (wrank + brank) // 2
            # categorize the elo into three categories
            if number >= 2000:
                number = 2000
            elif number >= 1500:
                number = 1500
            else:
                number = 1000
            opening = cur_game.headers["Opening"].split(":")[0].split(",")[0].split("#")[0]
            for move in cur_game.mainline_moves():
                squares[number][str(move)[:2]] += 1
                squares[number][str(move)[2:4]] += 1
                squares[opening][str(move)[2:4]] += 1
                squares[opening][str(move)[:2]] += 1
                # headers is for later if I want to use data on openings
            cur_game = chess.pgn.read_game(notated)
            # Go to next game
    write_json(squares)


def write_json(squares):
    with open('json_data.json', 'w') as json_file:
        json.dump(squares, json_file)


def obtain_json():
    try:
        with open('json_data.json', 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        return {}


if __name__ == "__main__":
    game_search()
