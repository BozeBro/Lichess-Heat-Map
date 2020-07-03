import json
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from database.filegrabber import file_grab
import json_handler.json_funcs as jf
import database.gameparser.datanavigator as dn
import heatmap.mapmaker as mm

# file_grab()
# Grab the file
# chess = dn.Parse("data.pgn")
# board = chess.game_search()
# Scan through the games
# jf.write_json(board)
# write json_folder
#chess.piece_search()
#FILE = 'json_data.json'
jf.write_json(chess.game_data, FILE)
data = jf.obtain_json(FILE)
games = list(data.keys())
print(games)
# See all game variations

gs = gridspec.GridSpec(2, 2)
# Treat the figure like a grid/plane
fig = plt.figure(figsize=(8, 5))

ax1 = fig.add_subplot(gs[0, 0])
# Use "1000", "1500" or "2000" to see games of people in those ranges
im, _ = mm.heatmap(data["French Defense"], "French ", ax=ax1, cmap="Reds")
mm.annotation(im, size=7)

ax2 = fig.add_subplot(gs[0, 1])
im, _ = mm.heatmap(data["King's Pawn Game"], "King", ax=ax2, cmap="Reds")
mm.annotation(im, size=7)

ax3 = fig.add_subplot(gs[1, 0])
im, _ = mm.heatmap(data["Queen's Pawn Game"], "Queen", ax=ax3, cmap="Reds")
mm.annotation(im, size=7)

ax4 = fig.add_subplot(gs[1, 1])
im, _ = mm.heatmap(total, "All games", ax=ax4, cmap="Reds")
mm.annotation(im, size=7)

plt.tight_layout()
# plt.savefig(r'C:\Users\benoz\Desktop\chess.jpg')
plt.show()
