import turtle

def main():
    global timmy
    
    timmy = turtle.Turtle()
    timmy.speed(0)

    square(200, -50, 75)
    square(25, -25, 50)
    square(25, 0, 50)
    square(25, -25, 25)
    square(25, 0, 25)
    square(25, 75, 50)
    square(25, 100, 50)
    square(25, 75, 25)
    square(25, 100, 25)
    rectangle(50, 75, 25, -50)
    square(5,65,-85)


def rectangle(width, height, x_start, y_start):
    timmy.penup()
    timmy.goto(x_start,y_start)
    timmy.pendown()
    timmy.forward(width)
    timmy.right(90)
    timmy.forward(height)
    timmy.right(90)
    timmy.forward(width)
    timmy.right(90)
    timmy.forward(height)
    timmy.right(90)

def square(width, x_start, y_start):
    rectangle(width, width, x_start, y_start)

main()