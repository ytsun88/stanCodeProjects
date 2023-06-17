"""
File: babygraphics.py
Name: Yu-Tao Sun
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    dis = width // len(YEARS)
    return GRAPH_MARGIN_SIZE + year_index * dis


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Create a line that is GRAPH_MARGIN_SIZE away from the top of the canvas.
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)

    # Create a line that is GRAPH_MARGIN_SIZE away from the bottom of the canvas.
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # Put all the lines and years on the canvas as mentioned in the spec.
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT,
                           width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # Use color_count to determine which color to fill with
    color_count = 0

    for name in lookup_names:
        # If the number of inputs exceeds the length of COLORS, start recycling from COLORS[0].
        color_index = color_count % len(COLORS)

        # Use a list to store the indices put beside the lines.
        texts = []

        # Use a list to store the y coordinates of the lines.
        y = []

        for year in YEARS:
            if str(year) in name_data[name]:                # Elements in YEARS need to be cast from an int into a str.
                texts.append(name_data[name][str(year)])    # If the name is in the ranking for a certain year,
            else:                                           # put the ranking of the name into texts.
                texts.append('*')                           # Else, put '*' into texts.

        for text in texts:                                  # Change indices in texts to y coordinates,
            if text == '*':                                 # which can be used to draw the lines.
                y.append(MAX_RANK)
            else:
                y.append(int(text))

        for i in range(len(y) - 1):
            # Codes below define the coordinates of each data point so that lines can be drawn.
            # I normalize the y value so that lines will be inside the space we have defined before.
            x1 = get_x_coordinate(CANVAS_WIDTH, i)
            x2 = get_x_coordinate(CANVAS_WIDTH, i + 1)
            y1 = int(GRAPH_MARGIN_SIZE + y[i] / MAX_RANK * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE))
            y2 = int(GRAPH_MARGIN_SIZE + y[i + 1] / MAX_RANK * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE))

            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[color_index])

        for j in range(len(y)):
            # Codes below define the coordinates of the indices put beside data points.
            x3 = get_x_coordinate(CANVAS_WIDTH, j)
            y3 = int(GRAPH_MARGIN_SIZE + y[j] / MAX_RANK * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE))

            canvas.create_text(x3 + TEXT_DX, y3, text=name+" "+texts[j], anchor=tkinter.SW, fill=COLORS[color_index])

        # Move to next color after drawing the line and indexing the data.
        color_count += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
