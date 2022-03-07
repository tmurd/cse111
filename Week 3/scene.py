# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

# Import random to use random function for stars
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Un-comment this code to draw grid over scene to help place objects
    # draw_grid(canvas, scene_width, scene_height, 50, color="deepPink3")


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    # Draw sky background
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="midnightBlue")
    # Draw random stars
    draw_stars(canvas, scene_width, scene_height)
    # Draw a cloud
    draw_clouds(canvas, 200, 400)
    # Draw another cloud
    draw_clouds(canvas, 400, 350)
    # This is the moon
    draw_oval(canvas, 625, 375, 725, 475, fill="seashell")
    return

def draw_ground(canvas, scene_width, scene_height):
    # Draw ground background
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="lavenderBlush2")
    # Draw a snowman
    draw_snowman(canvas, 600, 50)
    # Draw another snowman
    draw_snowman(canvas, 700, 100)

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)
    return

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

# Draw grid to help place objects in scene
def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)

# Draw randomly placed stars in the sky
def draw_stars(canvas, width, height):
    for i in range(0, width):
        for j in range(175, height):
            if random.randint(0, 1500) == 50:
                draw_oval(canvas, i, j, i + 3, j + 3, fill="yellow1")

# Draw multiple ovals to create a cloud
def draw_clouds(canvas, start_x, start_y):
    draw_oval(canvas, start_x, start_y, start_x + 100, start_y + 50, width=0, fill="seashell")
    draw_oval(canvas, start_x - 25, start_y - 20, start_x + 50, start_y + 25, width=0, fill="seashell")
    draw_oval(canvas, start_x + 20, start_y - 20, start_x + 130, start_y + 25, width=0, fill="seashell")

def draw_snowman(canvas, start_x, start_y):
    # draw body
    draw_oval(canvas, start_x, start_y, start_x + 50, start_y + 50, width=1, fill="seashell")
    draw_oval(canvas, start_x, start_y + 30, start_x + 50, start_y + 80, width=1, fill="seashell")
    draw_oval(canvas, start_x, start_y + 60, start_x + 50, start_y + 110, width=1, fill="seashell") 
    # draw buttons
    draw_oval(canvas, start_x + 23, start_y + 53, start_x + 27, start_y + 58, width=0, fill="black")
    draw_oval(canvas, start_x + 23, start_y + 45, start_x + 27, start_y + 50, width=0, fill="black")
    draw_oval(canvas, start_x + 23, start_y + 38, start_x + 27, start_y + 43, width=0, fill="black")
    # draw eyes
    draw_oval(canvas, start_x + 10, start_y + 85, start_x + 15, start_y + 90, width=0, fill="black")
    draw_oval(canvas, start_x + 40, start_y + 85, start_x + 35, start_y + 90, width=0, fill="black")
    # draw arms
    draw_line(canvas, start_x + 2, start_y + 52, start_x - 20, start_y + 70, width=2, fill="brown")
    draw_line(canvas, start_x + 48, start_y + 52, start_x + 70, start_y + 70, width=2, fill="brown")
    # draw nose
    draw_line(canvas, start_x + 23, start_y + 80, start_x + 30, start_y + 75, width=2, fill="orange")

# Call the main function so that
# this program will start executing.
main()