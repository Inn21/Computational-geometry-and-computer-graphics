# 10. Реалізувати алгоритм  параболічної  інтерполяції.  
# Передбачити інтерактивний ввід та обробку інформації. 
# Показати на кожному етапі побудову складових парабол і усереднення їх. 
# Дослідити виконання граничних умов в точках з’єднання. 
# Показати вплив зміни параметрів в кінцевих точках.


import turtle
import numpy as np

def draw_parabola(t, x1, y1, x2, y2, x3, y3, color):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.pencolor(color)

    for u in np.linspace(0, 1, 100):
        x = (1 - u) ** 2 * x1 + 2 * (1 - u) * u * x2 + u ** 2 * x3
        y = (1 - u) ** 2 * y1 + 2 * (1 - u) * u * y2 + u ** 2 * y3
        t.goto(x, y)

def input_points():
    points = []
    n = int(input("Введіть кількість парабол для побудови: "))
    for i in range(n):
        print(f"\nПарабола {i + 1}:")
        x1, y1 = map(int, input("Введіть координати першої точки (x1 y1): ").split())
        x2, y2 = map(int, input("Введіть координати середньої точки (x2 y2): ").split())
        x3, y3 = map(int, input("Введіть координати кінцевої точки (x3 y3): ").split())
        points.append((x1, y1, x2, y2, x3, y3))
    return points

def example_points():
    return [
        (-400, 0, -200, 100, 0, 0),
        (0, 0, 50, -300, 100, 0),
        (80, 0, 100, 300, 400, 0)
    ]




screen = turtle.Screen()
screen.setup(width=800, height=600)
t = turtle.Turtle()
t.speed(1)

mode = input("Виберіть режим (1 - Інтерактивний ввід, 2 - Приклад даних): ")
if mode == '1':
    points = input_points()
else:
    points = example_points()

colors = ['red', 'blue', 'green', 'orange', 'purple']

for i, (x1, y1, x2, y2, x3, y3) in enumerate(points):
    draw_parabola(t, x1, y1, x2, y2, x3, y3, colors[i % len(colors)])

for i in range(1, len(points)):
    _, _, x2_prev, y2_prev, x3_prev, y3_prev = points[i - 1]
    x1_curr, y1_curr, _, _, _, _ = points[i]
    if (x3_prev, y3_prev) != (x1_curr, y1_curr):
        print(f"Граничні умови не виконуються між параболами {i} і {i + 1}")
    else:
        print(f"Граничні умови виконуються між параболами {i} і {i + 1}")

turtle.done()
