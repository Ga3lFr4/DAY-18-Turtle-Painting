import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.color("blue")


def draw_square(size):
    for _ in range(4):
        tim.fd(size)
        tim.left(90)


def draw_dashed_line(pace, dashes):
    for _ in range(dashes):
        tim.fd(pace)
        tim.penup()
        tim.fd(pace)
        tim.pendown()


def set_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color((r, g, b))


def draw_shapes(size, min_sides=3, max_sides=10):
    for i in range(min_sides, max_sides+1):
        angle = 360 / i
        set_random_color()
        for _ in range(i):
            tim.fd(size)
            tim.right(angle)


def random_walk(size, steps):
    tim.speed(10)
    tim.pensize(10)
    for _ in range(steps):
        set_random_color()
        tim.fd(size)
        direction = random.randrange(0, 271, 90)
        tim.setheading(direction)


def draw_spirograph(size, num_circles):
    tim.speed(0)
    angle = 360 / num_circles
    for _ in range(num_circles+1):
        set_random_color()
        tim.left(angle)
        tim.circle(size)


draw_dashed_line(10, 50)









screen = Screen()
screen.exitonclick()
