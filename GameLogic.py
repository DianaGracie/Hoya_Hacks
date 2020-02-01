from Player import Player
from Trash import Trash

class GameLogic:
	def __init__(self):
		self.x = 1

	def update(self, dt):
		self.x += dt