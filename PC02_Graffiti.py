#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

#turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

myturtle = turtle.Turtle()

#Navigating
myturtle.penup()
myturtle.goto(-300,140)
myturtle.pendown()

#Square1
myturtle.color("blue","green")
myturtle.begin_fill()
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(100)
myturtle.end_fill()


#Navigating
myturtle.penup()
myturtle.goto(-100,210)
myturtle.pendown()

#Circle

myturtle.color("red","yellow")
myturtle.pensize(6)
myturtle.begin_fill()
myturtle.circle(60)
myturtle.end_fill()

#Navigating
myturtle.penup()
myturtle.goto(100,-85)
myturtle.pendown()

#triangle
myturtle.color("pink","blue")
myturtle.pensize(10)
myturtle.begin_fill()
myturtle.forward(100)
myturtle.left(120)
myturtle.forward(100)
myturtle.left(120)
myturtle.forward(100)
myturtle.end_fill()

#Navigating
myturtle.penup()
myturtle.goto(5,64)
myturtle.pendown()

#line
myturtle.setheading(0)
myturtle.color("black")
myturtle.pensize(13)
myturtle.forward(30)


#Navigating
myturtle.penup()
myturtle.goto(16,-170)
myturtle.pendown()

#line_RGB_color
myturtle.setheading(280)
mycolor = (0.7, 0.99, 0.13)
myturtle.pencolor(mycolor)
myturtle.pencolor()
myturtle.pensize(45)
myturtle.forward(60)


#Navigating

myturtle.penup()
myturtle.setx(0)
myturtle.sety(0)
myturtle.goto(-300,0)
myturtle.pendown()

#Square2
myturtle.setheading(0)
myturtle.color("blue")
myturtle.pensize(15)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(100)





#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
