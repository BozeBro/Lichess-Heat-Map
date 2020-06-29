from database.filegrabber import file_grab
import database.datanavigator as dn
import heatmap.mapmaker as mm
import json
import matplotlib.pyplot as plt
# file_grab()
# dn.game_search()
data = dn.obtain_json()
rank = "2000"
im, cbar = mm.heatmap(data[rank], rank, cmap="Oranges", cbarlabel="Move Frequency")
plt.show()

