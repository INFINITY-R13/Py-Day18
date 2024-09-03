from turtle import Turtle, Screen

the_turtle = Turtle()
the_turtle.shape("turtle")
the_turtle.color("pink")

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
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        the_turtle.forward(69)
        the_turtle.right(angle)

for n in range(3, 11):
    draw_shape(n)        








my_screen = Screen()
my_screen.exitonclick()