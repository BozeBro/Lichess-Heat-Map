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
    for i, j in enumerate(board):
        board[i] = data[j]
    board = np.reshape(board, (8, 8))
    return board


def heatmap(data, rank, cbarlabel="", cbar_kw={}, **kwargs):
    """
    Creates a heatmap from numpy array, squares.
    :parameter
    ---------------
    data
        This is the json data that is from datanavigator.py

    :givens/chess notation
    ------------
    YAXES
        The number/column
    XAXES
        The rows represented by letter

    """
    chess_board = sort_data(data)
    XAXES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    YAXES = [8, 7, 6, 5, 4, 3, 2, 1]
    # Chess notation

    fig, ax = plt.subplots()
    im = ax.imshow(chess_board, **kwargs)
    # The heatmap object

    cbar = ax.figure.colorbar(im, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    ax.set_xticks(np.arange(len(XAXES)))
    ax.set_yticks(np.arange(len(YAXES)))

    ax.set_xticklabels(XAXES)
    ax.set_yticklabels(YAXES)

    plt.setp(ax.get_xticklabels(), rotation=0, ha="left",
             rotation_mode="anchor")
    plt.title(f'{rank} level players')
    return im, cbar


if __name__ == '__main__':
    print('Hello World')
