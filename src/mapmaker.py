import numpy as np
import matplotlib
import matplotlib.pyplot as plt

"""
Heatmaps in matplotlib is an imshow plot.
    imshow plot 'displays an image/ data on a 2d plane'.
"""


def sort_data(data):
    """
    This will parse the data so that it can be iterated over without
    checking it.
        Sorts first by its ord() value and then by its numerical value.
    """
    board = sorted(data, key=lambda x: (-int(x[1]), ord(x[0])))
    # makes board have notation of a chess_board
    board = [data[i] for i in board]
    # Add values in
    board = np.reshape(board, (8, 8))
    # Make the board into an 8 x 8 board
    return board



def heatmap(data, title="placeholder", ax=None, cbarlabel="Move Frequency", cbar_kw={"ticks": []}, **kwargs):
    """
    Creates a heatmap from numpy array, squares.
    Creates a colorbar showing how the color changes along with moves to a square
    :parameter
    ---------------
    data
        This is the json data that is from datanavigator.py
    title
        This gives the general rank of players for this data
    ax
        Allows plot to have multiple subplots in a figure
    cbarlabel (optional)
        The label for the colobar
            Preset is Move Frequency
    cbar_kw (optional)
        kwargs for the colorbar
    **kwargs (optional)
        kwargs for the imshow(), the heatmap

    :givens/chess notation
    ------------
    YAXES
        The number/column
    XAXES
        The rows represented by letter
    :defined
    ------------
    chess_board
        2D representation of the chess board
    amount
        Total amount of games played.
        Used to find percentages
    :return
        im(heatmap)
        cbar (colorbar)
    """
    if not ax:
        fig, ax = plt.subplots()
    chess_board = sort_data(data)

    XAXES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    YAXES = [8, 7, 6, 5, 4, 3, 2, 1]
    # Chess notation

    im = ax.imshow(chess_board, **kwargs)
    # The heatmap object

    cbar = ax.figure.colorbar(im, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
    # Create the colorbar
    ax.set_xticks(np.arange(len(XAXES)))
    ax.set_yticks(np.arange(len(YAXES)))

    ax.set_xticklabels(XAXES)
    ax.set_yticklabels(YAXES)

    plt.setp(ax.get_xticklabels(), rotation=0, ha="left",
             rotation_mode="anchor")
    plt.title(title)
    plt.tight_layout()
    # Stop any overlapping subplots
    return im, cbar


def annotation(im, crange=["white", "black"], valfmt="{x:.1f}", **textkw):
    """
    Annotates each square of the chessboard with the percentage of times a piece moves to that square.
    Will get the percentage by chess_board[square] / number
    :parameter:
    -----------
    im
        The heatmap
    crange
        The color of the text
            crange[0] when below a certain threshold
            crange[1] when above a threshold
    valfmt
        Text formatter
    **textkw
        kwargs for text object
    :return:
    ----------
    texts
        annotations object
    """
    numbers = im.get_array()
    total, threshold, texts = sum(sum(numbers)), \
                              im.norm(numbers.max() * 3 / 4), \
                              []
    # Used 3/4 so it is only darker squares having white texts
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    for i in range(numbers.shape[0]):
        for j in range(numbers.shape[1]):
            kw.update(color=crange[int(im.norm(numbers[i, j]) < threshold)])
            text = im.axes.text(j, i, valfmt(round(numbers[i, j] / total * 100, 1)), **kw)
            texts.append(text)
    # Iterate through the chess_board and add the text onto the square
    plt.tight_layout()
    # Fit words onto the square
    return texts
