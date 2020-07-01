from database.filegrabber import file_grab
import database.datanavigator as dn
import json
import heatmap.mapmaker as mm
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from collections import Counter
# To see heatmap of game variation, change the argument inside data[arg] to desired variation. e.g. data["Sicilian Defense"]
file_grab()
# Grab the file
dn.game_search()
# Scan through the games

data = dn.obtain_json()
games = list(data.keys())
# print(games)
# See all game variations
all_games = [data["1000"], data["1500"],
             data["2000"]]
counter = Counter()
for d in all_games:
    counter.update(d)
total = dict(counter)

gs = gridspec.GridSpec(2, 2)
# Treat the figure like a grid/plane
fig = plt.figure(figsize=(8, 5))

ax1 = fig.add_subplot(gs[0, 0])
# Use "1000", "1500" or "2000" to see games of people in those ranges
im, _ = mm.heatmap(data["1000"], "Below 1500", ax=ax1, cmap="OrRd")
mm.annotation(im, size=7)

ax2 = fig.add_subplot(gs[0, 1])
im, _ = mm.heatmap(data["1500"], "1500 to 2000", ax=ax2, cmap="Reds")
mm.annotation(im, size=7)

ax3 = fig.add_subplot(gs[1, 0])
im, _ = mm.heatmap(data["2000"], "2000 and above", ax=ax3, cmap="Reds")
mm.annotation(im, size=7)

ax4 = fig.add_subplot(gs[1, 1])
im, _ = mm.heatmap(total, "All games", ax=ax4, cmap="Reds")
mm.annotation(im, size=7)

plt.tight_layout()
plt.show()
