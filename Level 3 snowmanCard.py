
import turtle
from colors import *
from shapes import *
from random import randint

bgColor = colors['lightblue']

# Define global scoped variables
currentY = -200  #trunk Y position
trunkWidth = 40
trunkHeight = 80  #trunk height

# Define a turtle screen object
window = turtle.Screen()
window.bgcolor(bgColor)
window.title('Christmas Tree')

# Define a turtle pen object
myPen = turtle.Turtle()
myPen.speed(10)      

def showCardName():
    myPen.penup
    myPen.color(bgColor)
    myPen.goto(0,-300)
    myPen.color(colors['red'])
    myPen.write('Merry Christmas', align='center', font=('Arial',30,('bold')))
    myPen.hideturtle()
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
    
def drawTrunk():
    drawRectangle(myPen, colors['brown'], -20, currentY, trunkWidth, trunkHeight)

def drawTree():
    drawTrunk()
    y = currentY + trunkHeight  
    treeWidth = 350
    for i in range(0, 9):
        treeWidth = treeWidth - randint(30, 41)
        treeHeight = randint(25,50)
        x = 0 - treeWidth / 2
        drawRectangle(myPen, colors['green'], x, y, treeWidth, treeHeight)
        y = y + treeHeight
    drawStar (myPen, colors['yellow'], 0, y+40, 100)  
    
showCardName()
drawTree()
window.mainloop()

