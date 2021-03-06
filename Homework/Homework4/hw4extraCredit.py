#! /usr/bin/python
# File Name:     hw4extraCredit.py
# Programmer:    Raul Aguilar
# Date:          June 20, 2020
# 
# CS 138 1535 Homework 4 Extra Credit
# Write a program that allows the user to draw a simple house using
# five mouse clicks
#
# Algorithm:
# 1. Draw window and ask user to set corners of the house
# 2. Calculate the width of the house, determine the top and bottom of
# the house
# 3. Draw the house and set outline to random color
# 4. Ask to set the top-center of the door frame
# 5. Calculate 1/5 of the house width to find width of the door
# 6. Using the width of the door and bottom of the house, find the
# top-left and bottom-right points of the door frame
# 7. Draw the door
# 8. Ask to set center of window
# 9. Calculate 1/2 the door width for the window width
# 10. Determine top-left and bottom-right corners of window frame from
# center point
# 11. Draw the window
# 12. Ask to set the peak of the roof
# 13. Using points from the top of the house and peak, draw the roof
# 14. Click again to exit
#
from graphics import *
from random import randint
import math

def randomColor():
    r, g, b = randint(0,255), randint(0,255), randint(0,255)
    return color_rgb(r,g,b)

def main():
    win = GraphWin("Draw a house", 300, 300)
    win.setCoords(0.0, 0.0, 300.0, 300.0)
    
    # Set corners of house and draw rectangle
    message = Text(Point(150, 5), "Set the corners of your house")
    message.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p1.undraw()

    # draw house
    house = Rectangle(p1, p2)
    house.setOutline(randomColor())
    house.draw(win)

    # calculate data points
    houseWidth = max(p1.getX(), p2.getX()) - min(p1.getX(), p2.getX())
    topHouse = max(p1.getY(), p2.getY())
    bottomHouse = min(p1.getY(), p2.getY())
    
    # Draw door
    message.setText("Set the top of the door")
    p3 = win.getMouse()
    
    doorWidth = houseWidth/5
    
    p4 = Point(p3.getX()-(doorWidth/2), p3.getY()) # top-left point
    p5 = Point(p3.getX()+(doorWidth/2), bottomHouse) # bottom-right point
    door = Rectangle(p4, p5)
    door.setOutline(randomColor())
    door.draw(win)
    
    # Draw window
    message.setText("Set the center of the window")
    p6 = win.getMouse()

    windowWidth = doorWidth/4
    
    p7 = Point(p6.getX()-windowWidth, p6.getY()+windowWidth) # top-left point
    p8 = Point(p6.getX()+windowWidth, p6.getY()-windowWidth) # bottom-right point
    window = Rectangle(p7, p8)
    window.setOutline(randomColor())
    window.draw(win)

    # Draw roof
    message.setText("Set the peak of the roof")
    p9 = win.getMouse()
    
    p10 = Point(p1.getX(), topHouse)
    p11 = Point(p2.getX(), topHouse)
    roof = Polygon(p9, p10, p11)
    roof.setOutline(randomColor())
    roof.draw(win)

    # exit
    message.setText("Click anywhere to exit")
    win.getMouse()
    win.close()


main()