from turtle import Turtle, Screen

the_turtle = Turtle()
the_turtle.shape("turtle")
the_turtle.color("pink")

# Draw a square
# for _ in range(4):
#     the_turtle.forward(100)
#     the_turtle.left(90)

# Draw a dashed line
for _ in range(15):
    the_turtle.forward(10)
    the_turtle.penup()
    the_turtle.forward(10)
    the_turtle.pendown()









my_screen = Screen()
my_screen.exitonclick()