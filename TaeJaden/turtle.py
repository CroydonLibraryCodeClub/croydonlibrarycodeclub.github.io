#!/bin/python3

from turtle import *
from random import randint
speed(0)
penup()
goto(-140,140)

for step in range(16):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
ada =   Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 120)
ada.pendown()


bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160,100)
bob.pendown()

jeff = Turtle()
jeff.color('yellow')
jeff.shape('turtle')

jeff.penup()
jeff.goto(-160,80)
jeff.pendown()

dod = Turtle()
dod.color('orange')
dod.shape('turtle')

dod.penup()
dod.goto(-160,60)
dod.pendown()

ditto = Turtle()
ditto.color('turquoise')
ditto.shape('turtle')

ditto.penup()
ditto.goto(-160,40)
ditto.pendown()

george = Turtle()
george.color('green')
george.shape('turtle')

george.penup()
george.goto(-160,20)
george.pendown()

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  jeff.forward(randint(1,5))
  dod.forward(randint(1,5))
  ditto.forward(randint(1,5))
  george.forward(randint(1,5))