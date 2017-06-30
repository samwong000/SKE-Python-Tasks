import turtle
from colors import *
from shapes import *
from random import randint

bgColor = colors['white']

# Define global scoped variables
currentY = -200  #trunk Y position
trunkWidth = 40
trunkHeight = 80  #trunk height

# Define a turtle screen object
window = turtle.Screen()
window.bgcolor(bgColor)
window.title('Snowman')

# Define a turtle pen object
myPen = turtle.Turtle()
myPen.speed(10)      

def drawBackground():
    drawCircle(myPen, colors['lightblue'], 0, -300, 300)
    return

def drawSnowflakes():
    x = randint(30, 60)
    y = randint(30, 60)
    
    return

drawBackground()
window.mainloop()

