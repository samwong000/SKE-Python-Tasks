
def drawCircle(turtle, color, x, y, diameter):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.setheading(0)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(diameter)
    turtle.end_fill()
    turtle.hideturtle()
    return

def drawStar (turtle, color, x, y, size):
    length = size * .223
    turtle.penup()
    turtle.pensize(1)
    turtle.speed(10)
    turtle.goto(x, y)
    
    # turn myPen direction by 108degree in order to make the star pointing up
    turtle.setheading(108) 

    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()

    for i in range(0, 5):
        turtle.left(144)
        turtle.forward(length)
        turtle.right(72)
        turtle.forward(length)

    turtle.end_fill()
    turtle.hideturtle()
    return

def drawRectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()
    turtle.setheading(0)
    turtle.hideturtle()
    return   
