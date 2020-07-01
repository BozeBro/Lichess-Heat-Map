# LichessHeatMap
This is a heatmap of Player moves between different elo rankings
  It can also create heatmaps of game variations like "Sicilian Defense
  
# Main 
The file to run to Get the pgn file, parse it, and produce the heatmap all in one go

# Database
  # filegrabber
      Has the function (filegrab) to retrieve the desired pgn file and write it to a file
  # datanavigator
      Has the function (game_search) to parse the pgn file and json functions
# Heatmap
  # mapmaker
      has the function (heatmap) to produce the heatmap, colorbar and text annotations
