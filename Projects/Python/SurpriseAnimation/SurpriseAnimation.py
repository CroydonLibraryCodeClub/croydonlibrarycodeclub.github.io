import pgzrun
import time

TITLE = 'BOO!'
WIDTH = 480
HEIGHT = 360

hedgehog = Actor('hedgehog-a', (150, 272))
hedgehog.text = None
apple = Actor('apple', (351, 272))
apple.text = None
hedgehog.walk = ['hedgehog-a', 'hedgehog-b']

def think():
	hedgehog.text = 'Hmm..'
	step()

def step():
	hedgehog.image = hedgehog.walk[0]
	hedgehog.x += 3
	if hedgehog.colliderect(apple):
		surprise()
	else:
		hedgehog.walk.reverse()
		clock.schedule(step, 0.1)

def surprise():
	apple.image = 'ghost'
	apple.text = 'BOO!'
	hedgehog.image = 'hedgehog-d'
	hedgehog.text = None
	sounds.laugh.play()

def draw():
	screen.blit('background', (0, 0))
	hedgehog.draw()
	if hedgehog.text is not None:
		screen.draw.text(hedgehog.text, midbottom = hedgehog.midtop)
	apple.draw()

clock.schedule(think, 1.0)
pgzrun.go()
