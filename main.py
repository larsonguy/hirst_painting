# import colorgram
from turtle import Turtle, Screen
import random
# def tuple_a_color(color):
#     rgb_list = [color.rgb[0], color.rgb[1], color.rgb[2]]
#     return tuple(rgb_list)
#
#
# color_list = []
# colors = colorgram.extract('img.jpg', 30)
#
# for color in colors:
#     rgb_color = tuple_a_color(color)
#     color_list.append(rgb_color)
#
# print(color_list)
#
# # create a function that takes the  colors variable, loops through each color object (30 total). For each color object,
# #   adds the r, g, b to a tuple, then appends that to the colors_list.


color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
              (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
              (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
              (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
              (65, 66, 56)]

turtle = Turtle()
turtle.penup()
turtle.hideturtle()
screen = Screen()

screen.colormode(255)

# TODO 1. Have turtle draw a circle (radius 10) using a random selection from color_list
# TODO 2. Have Turtle move 50 spaces
def draw_circle():
    random_color = random.choice(color_list)
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)
    


y_pos = 0
# TODO 4. After 10x, have turtle move y_pos +50
# TODO 5. Repeat 1-4 10x

for _ in range(10):
    # TODO 3. Repeat 1-2 10 x
    for _ in range(10):
        draw_circle()
    y_pos += 50
    turtle.teleport(0, y_pos)






screen.exitonclick()