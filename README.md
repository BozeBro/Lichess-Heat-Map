# LichessHeatMap
This is a heatmap of Player moves between different elo rankings
  It can also create heatmaps of game variations like "Sicilian Defense
The actual site of the database can be found here https://database.lichess.org/ .

# main 
The file to run to Get the pgn file, parse it, and produce the heatmap all in one go
# ---------
  # filegrabber
      Has the function (filegrab) to retrieve the desired pgn file and write it to a file
  # datanavigator
      Has the function (game_search) to parse the pgn file and json functions
# ----------
  # mapmaker
      has the function (heatmap) to produce the heatmap, colorbar and text annotations
