import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [
    (204, 164, 107), (151, 73, 47), (239, 245, 240), (235, 237, 243), (52, 93, 124), (223, 201, 136), (169, 153, 41),
    (136, 32, 22), (132, 162, 185), (201, 91, 70), (48, 122, 88), (67, 47, 41), (14, 100, 73), (147, 178, 146),
    (162, 142, 157), (234, 175, 165), (111, 74, 77), (18, 85, 89), (183, 205, 172), (55, 45, 48), (154, 16, 20),
    (39, 61, 74), (49, 65, 79), (83, 146, 128), (178, 89, 93), (179, 191, 207), (110, 127, 150), (215, 177, 182)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()