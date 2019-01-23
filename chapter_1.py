import turtle 
sven = turtle.Turtle()
# ole = turtle.Turtle()
#this makes a square of any size!
import math
# colors = ['blue', 'orange', 'yellow', 'purple', 'green']

# def any_square(turtle, size):
#     for i in range(4):
#         turtle.forward(size)
#         turtle.right(90) 

# def sqr_root_shape(turtle):
#     counter = 0
#     for i in range(0, 500, 5):
#         turtle.forward(i)
#         turtle.right(135)
#         if counter >= len(colors):
#             counter -= 1
#             turtle.color(colors[counter])
#         elif counter < len(colors):
#             counter +=1 
#             turtle.color(colors[counter])

def polygon(t, size, sides):
    angle = 360 / sides
    for i in range(sides):
        t.forward(size)
        t.right(angle)


# def middle_circle(turtle, radius):
#     pi = 3.14515
#     circ = 2 * pi * radius
#     side_length = circ / 360
#     turtle.up()
#     turtle.left(90)
#     turtle.forward(radius)
#     turtle.right(90)
#     turtle.down()
#     turtle.begin_fill()
#     polygon(turtle, side_length, 360)
#     turtle.end_fill()


def flower(t, num_squares, size):
    wn = turtle.Screen()
    wn.bgcolor('blue')
    t.color('yellow')
    for i in range(num_squares):
        t.right(360 / num_squares)
        polygon(t, size, 4)
    
    wn.exitonclick()

flower(sven, 20, 100)



turtle.done()

