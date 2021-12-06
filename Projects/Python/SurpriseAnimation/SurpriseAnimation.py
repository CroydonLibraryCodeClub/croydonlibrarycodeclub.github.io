import pgzrun
import time

TITLE = 'BOO!'
WIDTH = 480
HEIGHT = 360

hedgehog = Actor('hedgehog-a', (200, 180))
hedgehog.text = None
apple = Actor('apple', (280, 180))
apple.text = None

def wait(seconds):
	end = time.time() + seconds
	while time.time() < end:
		yield

def hedgehog_script():
	hedgehog.pos = (150, 272)
	yield from wait(1.0)
	hedgehog.text = 'Hmm..'
	for _ in range(20):
		hedgehog.image = 'hedgehog-a'
		hedgehog.x += 3
		yield from wait(0.1)
		hedgehog.image = 'hedgehog-b'
		hedgehog.x += 3
		yield from wait(0.1)
	hedgehog.text = None
	yield from wait(1.0)
	hedgehog.image = 'hedgehog-d'

def apple_script():
	apple.pos = (351, 272)
	yield from wait(6.0)
	apple.image = 'ghost'
	apple.text = 'BOO!'
	sounds.laugh.play()

def update():
	done = []
	for script in scripts:
		try:
			next(script)
		except StopIteration:
			done.append(script)
	for script in done:
		scripts.remove(script)

def draw():
	screen.blit('background', (0, 0))
	for sprite in sprites:
		sprite.draw()
		if sprite.text is not None:
			screen.draw.text(
				sprite.text,
				midbottom = sprite.midtop
			)

sprites = [hedgehog, apple]
scripts = [hedgehog_script(), apple_script()]
pgzrun.go()
