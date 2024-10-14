import turtle
import math
import time

def rotate_point(x, y, cx, cy, angle):
    radians = math.radians(angle)

    translated_x = x - cx
    translated_y = y - cy
    
    rotated_x = translated_x * math.cos(radians) - translated_y * math.sin(radians)
    rotated_y = translated_x * math.sin(radians) + translated_y * math.cos(radians)
    
    new_x = rotated_x + cx
    new_y = rotated_y + cy
    return new_x, new_y

def draw_square(t, cx, cy, size):
    points = [
        (-size / 2, -size / 2),
        (size / 2, -size / 2),
        (size / 2, size / 2),
        (-size / 2, size / 2)
    ]

    points = [(x+cx, y+cy) for x, y in points]
    
    t.penup()
    t.goto(points[-1][0], points[-1][1])
    t.pendown()
    for x, y in points:
        t.goto(x, y)

def draw_triangle(t, cx, cy, size):
    height = math.sqrt(3) / 2 * size
    points = [
        (-size / 2, -height / 3),
        (size / 2, -height / 3),
        (0, 2 * height / 3)
    ]
    
    points = [(x+cx, y+cy) for x, y in points]

    t.penup()
    t.goto(points[-1][0], points[-1][1])
    t.pendown()
    for x, y in points:
        t.goto(x, y)

def draw_rotated_square(t, cx, cy, ref_x, ref_y, size, angle):    
    points = [
        (-size / 2, -size / 2),
        (size / 2, -size / 2),
        (size / 2, size / 2),
        (-size / 2, size / 2)
    ]
    
    points = [(x+cx, y+cy) for x, y in points]

    rotated_points = [rotate_point(x, y, ref_x, ref_y, angle) for x, y in points]
    
    t.penup()
    t.goto(rotated_points[-1])
    t.pendown()
    t.pencolor("red")
    for point in rotated_points:
        t.goto(point)

def draw_rotated_triangle(t, cx, cy, ref_x, ref_y, size, angle):
    height = math.sqrt(3) / 2 * size
    points = [
        (-size / 2, -height / 3),
        (size / 2, -height / 3),
        (0, 2 * height / 3)
    ]    
    points = [(x+cx, y+cy) for x, y in points]

    rotated_points = [rotate_point(x, y, ref_x, ref_y, angle) for x, y in points]
   
    t.penup()
    t.goto(rotated_points[-1])
    t.pendown()
    t.pencolor("red")
    for point in rotated_points:
        t.goto(point)
    t.pencolor("black")

screen = turtle.Screen()
screen.setup(width=800, height=600)
t = turtle.Turtle()
r = turtle.Turtle()
r.speed(0)
r.hideturtle()

center_x, center_y = 50, 0
rot_x, rot_y = 50, 100
size = 100
endAngle = 45
t.penup()
t.goto(center_x, center_y)
t.dot(5, "black")

t.penup()
t.goto(rot_x, rot_y)
t.dot(5, "red")

draw_square(t, center_x, center_y, size)
draw_triangle(t, center_x, center_y, size)

for angle in range(0, endAngle+1):
    draw_rotated_square(r, center_x, center_y, rot_x, rot_y, size, angle)
    draw_rotated_triangle(r, center_x, center_y, rot_x, rot_y, size, angle)
    if angle != endAngle:
        r.clear()

turtle.done()