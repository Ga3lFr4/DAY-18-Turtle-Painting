import turtle
import random
import colorgram
from turtle import Turtle, Screen

turtle.colormode(255)
turtle.setworldcoordinates(0, 0, 500, 500)
colors = colorgram.extract('image.jpg', 30)
tim = Turtle()
tim.hideturtle()


colors_rgb = []
for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    rgb = (r, g, b)
    colors_rgb.append(rgb)

tim.setpos(0, 0)
tim.pensize(20)
tim.speed(0)
color_list = [(253, 252, 246), (243, 254, 249), (253, 245, 251), (243, 245, 253), (213, 151, 106), (248, 247, 74), (87, 244, 200), (41, 12, 179), (224, 115, 161), (160, 10, 76), (17, 181, 76), (31, 6, 90), (223, 49, 138), (151, 88, 43), (118, 98, 228), (84, 34, 13), (9, 97, 45), (85, 6, 38), (183, 182, 241), (71, 216, 90), (178, 45, 104), (47, 16, 249), (34, 142, 47), (155, 134, 215), (173, 9, 7), (75, 244, 249), (228, 166, 205), (234, 47, 43), (87, 74, 148), (6, 96, 100)]



def set_random_color(my_list):
    choice = random.choice(my_list)
    r = choice[0]
    g = choice[1]
    b = choice[2]
    return (r, g, b)


def paint(dashes, pace, step):
    for _ in range(dashes):
        tim.setx(0)
        for _ in range(dashes):
            random_color = set_random_color(color_list)
            tim.pencolor(random_color)
            tim.pendown()
            tim.fd(pace)
            tim.penup()
            tim.fd(step)
        new_y = tim.ycor() + step
        tim.sety(new_y)


paint(10, 1, 50)



screen = Screen()
screen.exitonclick()
