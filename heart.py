#!/usr/bin/env python

# -*- coding:utf-8 -*- 

import turtle

import time

  

# Painted Heart-shaped arc

def hart_arc():

    for i in range(200):

        turtle.right(1)

        turtle.forward(2)

  

def move_pen_position(x, y):

    turtle.hideturtle()     #  Hide brush (first)

    turtle.up()     #  Pick up a pen

    turtle.goto(x, y)    #  Moving the brush to the designated start coordinates (0,0 window center)

    turtle.down()   #  Write

    turtle.showturtle()     #  Brush display

    

#  initialization

turtle.setup(width=800, height=500)     #  Window (canvas) size

turtle.color('red', 'pink')     #  Brush Color

turtle.pensize(3)       #  Brush thickness

turtle.speed(1)     #  Drawing speed

#  Initialization brush start coordinates

move_pen_position(x=0,y=-180)   #  Mobile brush location

turtle.left(140)    #  Rotating 140 degrees to the left

  

turtle.begin_fill()     #  BACKGROUND filling position marker

  

#  Videos Heart linear (bottom left)

turtle.forward(224)    #  The brush is moved forward, a length of 224

#  Love painting arc

hart_arc()      #  The left side of the arc

turtle.left(120)    #  Brush angle adjustment

hart_arc()      #  The right side of the arc

#  Videos Heart linear (bottom right)

turtle.forward(224)

  

turtle.end_fill()       #  Background fill mark end position

  

#  Click on the window to close the program

window = turtle.Screen()

window.exitonclick()
 