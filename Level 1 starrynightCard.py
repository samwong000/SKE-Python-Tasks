
import turtle
from colors import *
from shapes import *
from random import randint

bgColor = colors['black']

# Define a turtle screen object
window = turtle.Screen()
window.bgcolor(bgColor)
window.title('Starry Night')

# Define a turtle pen object
myPen = turtle.Turtle()
myPen.color(bgColor)
myPen.speed(10)   
    
def drawMoon():
    positions = [(220, 200, colors['white']), (200, 200, colors['black'])]
    diameter = 50
    for x, y, color in positions:
        drawCircle(myPen, color, x, y, diameter)
    return

def drawStars():
    noOfStars = 12
    # For loop to draw 12 stars
    for i in range(0, noOfStars):
        # Set random position and size of stars
        x = randint(-9, 9) * 30
        y = randint(-9, 9) * 20
        size = randint(1, 4) * 25
        # Call drawStar function
        drawStar(myPen, colors['white'], x, y, size)    
    return

def showCardName():
    myPen.penup
    myPen.goto(0,-300)
    myPen.color(colors['yellow'])
    myPen.write('Merry Christmas', align='center', font=('Arial',30,('bold')))
    myPen.hideturtle()
    return

showCardName()
drawMoon()
drawStars()
window.mainloop()

