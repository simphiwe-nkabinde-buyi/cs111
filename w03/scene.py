# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_sun(canvas, scene_width, scene_height)
    draw_clouds(canvas, scene_width, scene_height)



    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height, scene_width, scene_height / 3, width=0, fill="sky blue" )

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects in the ground."""
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="tan4" )

def draw_sun(canvas, scene_width, scene_height):
    """Draw the sun on the left hand corner"""
    diameter = 200
    x = 50
    y = scene_height - 20
    draw_oval(canvas, x, y, x + diameter, y - diameter, fill="gold")

def draw_clouds(canvas, scene_width, scene_height):
    """ Draw 15 ovals, each with a random location and diameter."""
    half_height = round(scene_height / 2)
    min_diam = 50
    max_diam = 60

    for i in range(15):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(half_height + 50, scene_height - 50)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter + 70, y + diameter, width=0, fill="white")


# Call the main function so that
# this program will start executing.
main()