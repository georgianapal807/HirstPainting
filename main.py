# import colorgram

# Extract all colors dots from the image.
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import random
import turtle
from turtle import Turtle,Screen

color_list = [(40, 45, 50), (185, 70, 26), (140, 28, 42), (180, 159, 35), (56, 106, 141), (225, 210, 91),
              (186, 172, 122), (56, 32, 24), (62, 21, 32), (118, 175, 189), (35, 49, 113), (160, 52, 82), (151, 30, 23),
              (28, 42, 38), (194, 82, 130), (79, 182, 76), (9, 98, 77), (114, 195, 162), (48, 114, 54), (229, 204, 10),
              (232, 76, 31), (64, 151, 168), (151, 211, 201), (183, 143, 163), (82, 67, 30), (79, 111, 183)]

turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.setheading(220)
tim.forward(300)
tim.setheading(0)
def random_color():
    color = random.choice(color_list)
    r = color[0]
    g = color[1]
    b = color[2]
    return r, g, b

for i in range(10):
    for _ in range(10):
        tim.dot(20, random_color())
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = Screen()
screen.exitonclick()