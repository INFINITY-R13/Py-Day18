from turtle import Turtle, Screen, colormode
import random

the_turtle = Turtle()
the_turtle.shape("turtle")
# the_turtle.color("pink")

# Draw a square
# for _ in range(4):
#     the_turtle.forward(100)
#     the_turtle.left(90)


# Draw a dashed line
# for _ in range(15):
#     the_turtle.forward(10)
#     the_turtle.penup()
#     the_turtle.forward(10)
#     the_turtle.pendown()


# Draw different shapes
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         the_turtle.forward(69)
#         the_turtle.right(angle)

# for n in range(3, 11):
#     draw_shape(n)        

# Random Walk
# colors = ['red', 'pink', 'yellow', 'green', 'blue', 'orange', 'purple']
# directions = [0, 90, 180, 270]
# the_turtle.pensize(13)
# the_turtle.speed("fastest")

# for _ in range(100):
#     the_turtle.color(random.choice(colors))
#     the_turtle.forward(30)
#     the_turtle.setheading(random.choice(directions))


# Draw a spirograph
colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

the_turtle.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        the_turtle.color(random_color())
        the_turtle.circle(100)
        the_turtle.setheading(the_turtle.heading() + size_of_gap)

draw_spirograph(10)




my_screen = Screen()
my_screen.exitonclick()