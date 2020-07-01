from database.filegrabber import file_grab
import database.datanavigator as dn
import heatmap.mapmaker as mm
import json
import matplotlib.pyplot as plt

file_grab()
dn.game_search(filed)
data = dn.obtain_json()
games = list(data.keys())
# See all game variations
rank = "1000"
# Use "1000", "1500" or "2000" to see games of people in those ranges
im, cbar = mm.heatmap(data[rank], rank, cmap="hsv", cbarlabel="Move Frequency")
texts = mm.annotation(im)
plt.show()

