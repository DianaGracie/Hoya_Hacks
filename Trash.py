from random import * 

class Trash:
	def __init__(self):
		self.pos = [random(), -0.1]

	def update(self, dt):
		self.pos[1] += dt
