from Player import Player
from Trash import Trash

class GameLogic:
	def __init__(self):
		self.state = "playing"
		self.p1 = Player(1)
		self.p2 = Player(2)
		self.trash_list = []

	def update(self, dt):
		self.p1.update(dt)
		self.p2.update(dt)