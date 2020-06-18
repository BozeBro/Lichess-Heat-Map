import chess.pgn
from pgn_parser import parser, pgn
from collections import defaultdict

"""
cur_game acts as an iterator that iterates through the pgn file
game will parse the game moves in an easy and simple way to manipulate  
"""

with open('test.pgn') as notated:
    cur_game = chess.pgn.read_game(notated)
    bUsed = wUsed = defaultdict(int)
    while cur_game:
        game = parser.parse(str(cur_game.mainline_moves()),
                            actions=pgn.Actions())

        for move in game.movetext:
            if move.white.san:
                wUsed[move.white.san[0]] += 1

            if move.black.san:
                bUsed[move.black.san[0]] += 1
        cur_game = chess.pgn.read_game(notated)
print('First Phase complete')

for i, v in wUsed.items():
    print(i, v)
for i, v in bUsed.items():
    print(i, v)