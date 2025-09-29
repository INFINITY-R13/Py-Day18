# ==================================
# 1. IMPORTS & INITIAL SETUP
# ==================================
from turtle import Turtle, Screen, colormode
import random

# Create a Screen object (this is the window)
my_screen = Screen()
my_screen.title("My Turtle Art")  # Optional: Give the window a title

# Set the colormode to 255. This allows us to use RGB color values from 0-255.
colormode(255)

# Create a Turtle object (this is our "pen" or "artist")
the_turtle = Turtle()
the_turtle.shape("turtle")
the_turtle.speed("fastest")  # Set drawing speed to maximum for faster results

# ==================================
# 2. FUNCTION DEFINITIONS
# ==================================

def random_color():
    """Generates and returns a random RGB color as a tuple."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_shape(num_sides, size=100):
    """Draws a regular polygon with a given number of sides and length."""
    angle = 360 / num_sides
    for _ in range(num_sides):
        the_turtle.forward(size)
        the_turtle.right(angle)

def draw_spirograph(gap_size):
    """Draws a spirograph by repeatedly drawing circles at tilted angles."""
    # Loop 360 degrees, stepping by the gap_size each time
    for _ in range(int(360 / gap_size)):
        the_turtle.color(random_color())
        the_turtle.circle(100)  # Draw a circle with a radius of 100
        # Tilt the turtle's heading for the next circle
        the_turtle.setheading(the_turtle.heading() + gap_size)


# ==================================
# 3. DRAWING EXAMPLES
# ==================================
# Instructions: Uncomment ONE of the blocks below to see it run.
# To uncomment, remove the '#' from the beginning of each line in the desired block.

# --- Example 1: Draw a Square ---
# the_turtle.color("red")
# draw_shape(4, size=150) # Use our function to draw a 4-sided shape


# --- Example 2: Draw a Dashed Line ---
# for _ in range(15):
#     the_turtle.forward(10)
#     the_turtle.penup()
#     the_turtle.forward(10)
#     the_turtle.pendown()


# --- Example 3: Draw a Row of Polygons (IMPROVED - No overlap) ---
# # Move turtle to a starting position on the left side of the screen
# the_turtle.penup()
# the_turtle.goto(-350, 0)
# the_turtle.pendown()
#
# # List of colors for our shapes
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# # Draw shapes from a triangle (3 sides) to a decagon (10 sides)
# for i, num_sides in enumerate(range(3, 11)):
#     the_turtle.color(colors[i])
#     draw_shape(num_sides, size=60)
#     # After drawing a shape, lift the pen and move to the next position
#     the_turtle.penup()
#     the_turtle.forward(100) # Move to create space
#     the_turtle.pendown()


# --- Example 4: Random Walk ---
# directions = [0, 90, 180, 270]  # East, North, West, South
# the_turtle.pensize(15)  # Make the line thicker
#
# for _ in range(200):
#     the_turtle.color(random_color())
#     the_turtle.forward(30)
#     the_turtle.setheading(random.choice(directions))


# --- Example 5: Draw a Spirograph ---
# # A smaller gap size (e.g., 5) creates a denser, more complex pattern
# draw_spirograph(gap_size=5)


# ==================================
# 4. EXIT
# ==================================
# This keeps the window open until you click on it. It should always be the last line.
my_screen.exitonclick()
