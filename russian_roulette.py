import turtle
from random import randrange
from math import sin, cos, pi


def go_to(center=()):
    my_turtle.penup()
    my_turtle.goto(center[0], center[1])
    my_turtle.pendown()


def draw_circle(radius, color, center=()):
    go_to(center)
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()


def get_x_and_y(center, angle_in_deg, radius, shift):
    angle = angle_in_deg * pi / 180
    x = center[0] + radius * sin(angle)
    y = center[1] + radius * cos(angle) + shift
    return x, y


def revolver(size_of_gun, center=()):
    draw_circle(80, 'white', center)
    draw_circle(5, 'red', (center[0], center[1] + 160))
    for position in range(circle_number):
        x, y = get_x_and_y(center, size_of_gun['phi'] * position, size_of_gun['small_radius'], size_of_gun['shift'])
        draw_circle(22, 'white', (x, y))


def rotation(center, start_position, size_of_gun):
    end = randrange(circle_number, 70)
    you_lose = False
    x = 0
    y = 0
    for i in range(start_position, end + 1):
        if end % circle_number == 0:
            you_lose = True
        x, y = get_x_and_y(center, size_of_gun['phi'] * i, size_of_gun['small_radius'], size_of_gun['shift'])
        draw_circle(22, 'brown', (x, y))
        draw_circle(22, 'white', (x, y))

    draw_circle(22, 'brown', (x, y))
    return [end, you_lose]


def game(size_of_gun, center, result_point):
    start = 0
    answer = ''
    while answer != 'n':
        answer = turtle.Screen().textinput('Play?', 'y/n')
        if answer == 'y':
            my_turtle.undo()
            my_turtle.color('black')
            result = rotation(center, start, size_of_gun)
            start = result[0] % circle_number
            go_to(result_point)
            turtle.Screen()
            if result[1]:
                my_turtle.color('red')
                my_turtle.write('You lose!', align='center', font=('Times New Roman', 32, 'normal'))
            else:
                my_turtle.color('green')
                my_turtle.write('You win!', align='center', font=('Times New Roman', 32, 'normal'))
        else:
            pass


if __name__ == '__main__':
    circle_number = 6
    size = {
        'phi': 360 / circle_number,
        'small_radius': 50,
        'shift': 58
    }
    center_point = (0, 0)
    point_for_result = (0, -150)

    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    my_turtle.hideturtle()
    revolver(size, center_point)
    game(size, center_point, point_for_result)
