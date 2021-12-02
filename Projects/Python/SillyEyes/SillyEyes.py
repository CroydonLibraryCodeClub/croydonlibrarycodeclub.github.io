import pgzrun
import random

TITLE = 'Silly Eyes'
WIDTH = 480
HEIGHT = 360

left_eye = Actor('eyeball', (200, 180))
right_eye = Actor('eyeball', (280, 180))

def on_mouse_move(pos):
	left_eye.angle = left_eye.angle_to(pos)
	right_eye.angle = right_eye.angle_to(pos)

def draw():
	left_eye.draw()
	right_eye.draw()

pgzrun.go()
