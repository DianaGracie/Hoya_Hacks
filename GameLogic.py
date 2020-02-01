from Player import Player
from Trash import Trash

class GameLogic:
	def __init__(self):
		self.p1 = Player(1)
		self.p2 = Player(2)
		self.trash_list = []

	def update(self, dt):
		pass