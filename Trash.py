from random import * 

class Trash:
	def __init__(self):
		x_pos = random()
		while (x_pos > .93):
			x_pos = random()
		self.pos = [x_pos, -100]
		self.id = randint(1,14)
		self.isTrash = True

	def update(self, dt):
		self.pos[1] += dt * 0.1
