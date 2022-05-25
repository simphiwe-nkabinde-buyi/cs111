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
    draw_trees(canvas, scene_width, round(scene_height/3.5))



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
    
def draw_trees(canvas, scene_width, ground_height):
    """draw multiple trees across the grounds"""
    max_bottom = ground_height
    for i in range(30):
        center_x = random.randint(0, scene_width)
        bottom = max_bottom#random.randint(0, max_bottom)
        height = random.randint(80, 120)
        max_bottom = max_bottom - 5
        draw_pine_tree(canvas, center_x, bottom, height)
        

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()