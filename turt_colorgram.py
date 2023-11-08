'''import colorgram

rgb_colors = []
colors = colorgram.extract('1.jpg', 30)
for color in colors:
    #rgb_colors.append(color.rgb)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
    
print(rgb_colors)'''
import turtle as t_module
import random

tim = t_module.Turtle()
t_module.colormode(255)
color_list = [(240, 245, 242), (236, 239, 243), (153, 75, 49), (222, 201, 136), (53, 94, 124), (171, 153, 41), (136, 32, 21), (133, 163, 184), (197, 93, 73), (48, 123, 87), (73, 44, 36), (14, 97, 72), (145, 178, 148), (91, 73, 75), (233, 176, 165), (160, 143, 159), (54, 47, 50), (184, 205, 172), (35, 61, 75), (22, 85, 89), (146, 19, 21), (86, 146, 130), (38, 67, 91), (13, 72, 66), (106, 128, 155), (175, 99, 101), (176, 192, 209)]

tim.speed("fastest")
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)
tim.pendown()
num_of_dots = 100
for dot_count in range(1,num_of_dots + 1):
    
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    tim.pendown()
    if dot_count % 10 == 0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

t_module.done()

